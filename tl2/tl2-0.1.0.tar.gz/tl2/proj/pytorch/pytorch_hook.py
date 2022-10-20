import time
from itertools import chain
import os
import sys
from operator import attrgetter
import pickle
from typing import Dict, Iterable, Callable, Tuple
import copy
import unittest
from termcolor import cprint
import logging
from functools import partial

import torch
from torch import nn, Tensor

from tl2.tl2_utils import TermColor, attrgetter_default
from tl2.proj.pytorch import torch_utils
from tl2 import tl2_utils

__all__ = ["VerboseModel", "FeatureExtractor", "GradExtractor", ]


class VerboseModel(nn.Module):
  def __init__(self,
               model: nn.Module,
               submodels=None,
               name_prefix="",
               register_itself=False,
               register_children=True,
               add_newline=True,
               input_padding=36,
               **kwargs):
    super().__init__()
    self.add_newline = add_newline
    self.input_padding = input_padding

    try:
      self.model = copy.deepcopy(model)
    except:
      self.model = pickle.loads(pickle.dumps(model))

    term_color = TermColor()

    # Register a hook for each layer
    if register_children:
      modules = self.model.named_children()
    else:
      modules = []
    if register_itself:
      modules = chain([("", self.model)], modules)
      self.model.__term_color__ = term_color.green

    for name, layer in modules:
      class_name = attrgetter_default(layer, "__class__.__name__", default='')
      layer.__name__ = f"{name_prefix}{name} ({class_name})"
      if not hasattr(layer, '__term_color__'):
        layer.__term_color__ = term_color.black
      layer.register_forward_hook(self._hook())

    if submodels is not None:
      if not isinstance(submodels, (list, tuple)):
        submodels = list(submodels)
      for submodel in submodels:
        color = term_color.get_a_color()
        sub_module = attrgetter(submodel)(self.model)
        for name, layer in sub_module.named_children():
          class_name = attrgetter_default(layer, "__class__.__name__", default='')
          layer.__name__ = f"{name_prefix}{submodel}.{name} ({class_name})"
          layer.__term_color__ = color
          layer.register_forward_hook(self._hook())
    pass

  def _hook(self, ) -> Callable:
    def fn(layer, input, output):
      input_shape = f"in({len(input)}): "
      for elem in input:
        if hasattr(elem, 'shape') and elem.nelement() > 0:
          input_shape += f"{str(list(elem.shape))}"
          min_max = f"({elem.min():.2f}, {elem.max():.2f}, m{elem.mean():.2f}, s{elem.std():.2f}), "
          input_shape += min_max
        else:
          input_shape += f"{type(elem)}, "

      input_shape = input_shape.strip(" ,")
      # if self.add_newline:
      #   input_shape += "\n"

      if not isinstance(output, tuple):
        output = (output, )
      output_shape = f"out({len(output)}): "
      for elem in output:
        if hasattr(elem, 'shape'):
          output_shape += f"{str(list(elem.shape))}"
          min_max = f"({elem.min():.2f}, {elem.max():.2f}, m{elem.mean():.2f}, s{elem.std():.2f}), "
          output_shape += min_max
        else:
          output_shape += f"{type(elem)}, "
      output_shape = output_shape.strip(" ,")

      num_params = sum([p.data.nelement() for p in layer.parameters()])/1e6
      num_bufs = sum([p.data.nelement() for p in layer.buffers()])
      param_str = f"{'':<{1}} paras: {str(num_params)}M "
      param_str = f"{param_str:<{19}}bufs: {str(num_bufs)}M"

      layer_str = str(layer)
      if '\n' in layer_str:
        layer_str = ''
      min_max_v = self._get_parameters_min_max_values(layer=layer, attr_name='weight')
      if min_max_v:
        layer_str += f", {min_max_v}"
      min_max_v = self._get_parameters_min_max_values(layer=layer, attr_name='bias')
      if min_max_v:
        layer_str += f", {min_max_v}"

      cprint(f"{(layer.__name__ + ': '):<{self.input_padding}}{input_shape}"             
             f"\n"
             f"{param_str:<{self.input_padding - 3}}=>{output_shape}"
             f"{'':<{3}} {layer_str}"
             , color=layer.__term_color__)

    return fn

  def _get_parameters_min_max_values(self, layer, attr_name):
    min_max_str = ""
    if hasattr(layer, attr_name):
      with torch.no_grad():
        p = getattr(layer, attr_name)
        if p is None:
          return f"{attr_name}({p})"
        min_v = p.min()
        max_v = p.max()
        min_max_str = f"{attr_name}({min_v:.2f}, {max_v:.2f}, m{p.mean():.2f})"
    return min_max_str


  def forward(self, *args, **kwargs) -> Tensor:
    return self.model(*args, **kwargs)

  @staticmethod
  def forward_verbose(model: nn.Module,
                      inputs_args: Tuple = None,
                      inputs_kwargs: Dict = None,
                      submodels=None,
                      name_prefix="",
                      register_itself=True,
                      register_children=True,
                      add_newline=True,
                      input_padding=36,
                      verbose=True,
                      **kwargs
                      ):
    with torch.no_grad():
      model_ver = VerboseModel(model=model,
                               submodels=submodels,
                               name_prefix=name_prefix,
                               register_itself=register_itself,
                               register_children=register_children,
                               add_newline=add_newline,
                               input_padding=input_padding,
                               )
      if inputs_args is None:
        inputs_args = ()
      if inputs_kwargs is None:
        inputs_kwargs = {}
      # inputs_args = copy.deepcopy(inputs_args)
      # inputs_kwargs = copy.deepcopy(inputs_kwargs)
      time_start = time.time()
      out = model_ver(*inputs_args, **inputs_kwargs)
      elapsed = time.time() - time_start
      del model_ver, out

      if verbose:
        torch_utils.print_number_params({name_prefix: model}, add_info=f"time: {elapsed:.4f}")
    return

class FeatureExtractor(nn.Module):
  def __init__(self, model: nn.Module, layers: Iterable[str]):
    super().__init__()
    self.model = model
    self.layers = layers
    self._features = {layer: torch.empty(0) for layer in layers}

    for layer_id in layers:
      layer = dict([*self.model.named_modules()])[layer_id]
      layer.register_forward_hook(self.save_outputs_hook(layer_id))
    pass

  def save_outputs_hook(self, layer_id: str) -> Callable:
    def fn(_, __, output):
      self._features[layer_id] = output
    return fn

  def forward(self, *args, **kwargs) -> Dict[str, Tensor]:
    self._features.clear()
    _ = self.model(*args, **kwargs)
    return self._features


class FeatureExtractor_v1(nn.Module):
  def __init__(self, model: nn.Module, layers: Iterable[str]):
    super().__init__()
    self.model = model
    self.layers = layers
    self._features = {layer: torch.empty(0) for layer in layers}

    for layer_id in layers:
      layer = dict([*self.model.named_modules()])[layer_id]
      layer.register_forward_hook(self.save_outputs_hook(layer_id))
    pass

  def save_outputs_hook(self, layer_id: str) -> Callable:
    hook = partial(self.fn, _features=self._features, layer_id=layer_id)
    return hook

  @staticmethod
  def fn(_, __, output, _features, layer_id):
    _features[layer_id] = output

  def forward(self, *args, **kwargs):
    self._features.clear()
    _ = self.model(*args, **kwargs)

    out = {k: v for k, v in self._features.items()}
    self._features.clear()

    return out



class GradExtractor(nn.Module):
  def __init__(self, model: nn.Module, param_names: Iterable[str]=[]):
    super().__init__()
    self.model = model
    self.param_names = param_names
    self._grads = {}

    for name, param in model.named_parameters():
      print(f"{name:<30}: {list(param.shape)}")
      if name in self.param_names:
        param.register_hook(hook=self._hook(name))
    pass

  def _hook(self, name: str) -> Callable:
    def fn(grad):
      self._grads[name] = grad.clone()
      return grad
    return fn

  def forward(self, x: Tensor) -> Dict[str, Tensor]:
    self._grads.clear()
    out = self.model(x)
    return out



class PytorchHook(unittest.TestCase):

  def test_register_forward_hook(self):

    import torch
    import torch.nn as nn

    class TestForHook(nn.Module):
      def __init__(self):
        super().__init__()

        self.linear_1 = nn.Linear(in_features=2, out_features=2)
        self.linear_2 = nn.Linear(in_features=2, out_features=1)
        self.relu = nn.ReLU()
        self.relu6 = nn.ReLU6()
        self.initialize()

      def forward(self, x):
        linear_1 = self.linear_1(x)
        linear_2 = self.linear_2(linear_1)
        relu = self.relu(linear_2)
        relu_6 = self.relu6(relu)
        layers_in = (x, linear_1, linear_2)
        layers_out = (linear_1, linear_2, relu)
        return relu_6, layers_in, layers_out

      def initialize(self):
        """ 定义特殊的初始化，用于验证是不是获取了权重"""
        self.linear_1.weight = torch.nn.Parameter(torch.FloatTensor([[1, 1], [1, 1]]))
        self.linear_1.bias = torch.nn.Parameter(torch.FloatTensor([1, 1]))
        self.linear_2.weight = torch.nn.Parameter(torch.FloatTensor([[1, 1]]))
        self.linear_2.bias = torch.nn.Parameter(torch.FloatTensor([1]))
        return True

    # 1：定义用于获取网络各层输入输出tensor的容器
    # 并定义module_name用于记录相应的module名字
    module_name = []
    features_in_hook = []
    features_out_hook = []

    # 2：hook函数负责将获取的输入输出添加到feature列表中
    # 并提供相应的module名字
    def hook(module, fea_in, fea_out):
      print("hooker working")
      module_name.append(module.__class__)
      features_in_hook.append(fea_in)
      features_out_hook.append(fea_out)
      return None

    # 3：定义全部是1的输入
    x = torch.FloatTensor([[0.1, 0.1], [0.1, 0.1]])

    # 4:注册钩子可以对某些层单独进行
    net = TestForHook()
    net_chilren = net.children()
    for child in net_chilren:
      if not isinstance(child, nn.ReLU6):
        child.register_forward_hook(hook=hook)

    # 5:测试网络输出
    out, features_in_forward, features_out_forward = net(x)
    print("*" * 5 + "forward return features" + "*" * 5)
    print(features_in_forward)
    print(features_out_forward)
    print("*" * 5 + "forward return features" + "*" * 5)

    # 6:测试features_in是不是存储了输入
    print("*" * 5 + "hook record features" + "*" * 5)
    print(features_in_hook)
    print(features_out_hook)
    print(module_name)
    print("*" * 5 + "hook record features" + "*" * 5)

    # 7：测试forward返回的feautes_in是不是和hook记录的一致
    print("sub result")
    for forward_return, hook_record in zip(features_in_forward, features_in_hook):
      print(forward_return - hook_record[0])

    pass

  def test_VerboseModel(self):

    from torchvision.models.segmentation import deeplabv3_resnet101

    verbose_resnet = VerboseModel(deeplabv3_resnet101(pretrained=True), submodels=['backbone', 'classifier', ])
    dummy_input = torch.ones(10, 3, 256, 256)
    _ = verbose_resnet(dummy_input)

    pass

  def test_VerboseModel_register_itself(self):

    import torch

    net = torch.nn.Linear(256, 512)
    net_ver = VerboseModel(net, register_itself=True)
    dummy_input = torch.ones(10, 256)
    out = net_ver(dummy_input)

    net = torch.nn.Sequential(
      torch.nn.Linear(256, 512)
    )
    net_ver = VerboseModel(net, register_itself=True, name_prefix='linear.')
    dummy_input = torch.ones(10, 256)
    out = net_ver(dummy_input)

    pass

  def test_VerboseModel_multi_input(self):

    import torch

    class FiLMLayer(nn.Module):
      def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.layer = nn.Linear(input_dim, hidden_dim)

      def forward(self, x, freq, phase_shift):
        x = self.layer(x)
        freq = freq.unsqueeze(1).expand_as(x)
        phase_shift = phase_shift.unsqueeze(1).expand_as(x)
        out = torch.sin(freq * x + phase_shift)
        return out, out

    net = FiLMLayer(256, 512)
    net_ver = VerboseModel(net, name_prefix="FiLM.", register_itself=True, register_children=False)
    x = torch.randn(2, 12, 256)
    freq = torch.randn(2, 512)
    phase = torch.randn(2, 512)
    out = net_ver(x, freq, phase)

    pass

  def test_FeatureExtractor(self):

    from torchvision.models import resnet50

    verbose_resnet = VerboseModel(resnet50(), submodels=['layer1', 'layer4', 'layer4.2'])
    dummy_input = torch.ones(10, 3, 224, 224)
    verbose_resnet(dummy_input)

    resnet_features = FeatureExtractor(resnet50(), layers=["layer4.2.relu", "avgpool", ])
    features = resnet_features(dummy_input)

    print({name: output.shape for name, output in features.items()})

    pass

  def test_GradExtractor(self):

    from torchvision.models import resnet50

    resnet_grad = GradExtractor(resnet50(), param_names=['fc.weight', 'conv1.weight'])
    dummy_input = torch.ones(10, 3, 224, 224)

    out = resnet_grad(dummy_input)
    loss = out.mean()
    loss.backward()
    grads = resnet_grad._grads
    print({name: output.mean() for name, output in grads.items()})

    pass

  def test_register_hook_grad(self):

    import torch

    y_grad = list()
    def grad_hook(grad):
      y_grad.append(grad)

    x = torch.tensor([2., 2., 2., 2.], requires_grad=True)
    y = torch.pow(x, 2)
    z = torch.mean(y)

    h = y.register_hook(grad_hook)

    z.backward()
    print("y.grad: ", y.grad)
    print("y_grad[0]: ", y_grad[0])
    h.remove()  # removes the hook
    pass

  def test_register_hook_scale_grad(self):

    import torch

    def grad_hook(grad):
      grad *= 2

    x = torch.tensor([2., 2., 2., 2.], requires_grad=True)
    y = torch.pow(x, 2)
    z = torch.mean(y)
    h = x.register_hook(grad_hook)
    z.backward()
    print(x.grad)
    h.remove()  # removes the hook

    pass

  def test_hook_for_grad_cam(self, debug=True):

    """
    Usage:
        python template_lib/modelarts/scripts/copy_tool.py \
          -s s3://bucket-7001/ZhouPeng/pypi/torch1_7_0 -d /cache/pypi -t copytree
        for filename in /cache/pypi/*.whl; do
            pip install $filename
        done
        proj_root=moco-exp
        python template_lib/modelarts/scripts/copy_tool.py \
          -s s3://bucket-7001/ZhouPeng/codes/$proj_root -d /cache/$proj_root -t copytree -b /cache/$proj_root/code.zip
        cd /cache/$proj_root
        pip install -r requirements.txt

        export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
        export TIME_STR=1
        export PYTHONPATH=./exp:./stylegan2-pytorch:./
        python 	-c "from exp.tests.test_styleganv2 import Testing_stylegan2;\
          Testing_stylegan2().test_train_ffhq_128()"

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'
    from tl2.launch.launch_utils import \
      (get_command_and_outdir, setup_outdir_and_yaml, get_append_cmd_str, start_cmd_run)

    tl_opts = ' '.join(sys.argv[sys.argv.index('--tl_opts') + 1:]) if '--tl_opts' in sys.argv else ''
    print(f'tl_opts:\n {tl_opts}')

    command, outdir = get_command_and_outdir(self, func_name=sys._getframe().f_code.co_name, file=__file__)
    argv_str = f"""
                --tl_config_file none
                --tl_command none
                --tl_outdir {outdir}
                --tl_opts {tl_opts}
                """
    args, cfg = setup_outdir_and_yaml(argv_str, return_cfg=True)

    n_gpus = len(os.environ['CUDA_VISIBLE_DEVICES'].split(','))
    cmd_str = f"""
        python 
        template_lib/proj/pytorch/examples/hook_for_grad_cam.py
        {get_append_cmd_str(args)}
        """
    if debug:
      cmd_str += f"""
                  --tl_debug
                  --tl_opts 
                  """
    else:
      cmd_str += f"""
                  --tl_opts {tl_opts}
                  """
    start_cmd_run(cmd_str)
    # from template_lib.v2.config_cfgnode import update_parser_defaults_from_yaml, global_cfg
    # from template_lib.modelarts import modelarts_utils
    # update_parser_defaults_from_yaml(parser)

    # modelarts_utils.setup_tl_outdir_obs(global_cfg)
    # modelarts_utils.modelarts_sync_results_dir(global_cfg, join=True)
    # modelarts_utils.prepare_dataset(global_cfg.get('modelarts_download', {}), global_cfg=global_cfg)
    #
    # modelarts_utils.prepare_dataset(global_cfg.get('modelarts_upload', {}), global_cfg=global_cfg, download=False)
    # modelarts_utils.modelarts_sync_results_dir(global_cfg, join=True)

    pass









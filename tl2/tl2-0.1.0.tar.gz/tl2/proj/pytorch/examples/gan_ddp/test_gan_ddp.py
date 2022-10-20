import time
from pathlib import Path
import os
import sys
import unittest
import argparse


class Testing_gan_ddp(unittest.TestCase):

  def test_train(self, debug=True):
    """
    Usage:

        # export CUDA_VISIBLE_DEVICES=$cuda_devices
        # export RUN_NUM=$run_num

        export CUDA_VISIBLE_DEVICES=7
        export TIME_STR=0
        export PORT=12345
        export PYTHONPATH=.:./piGAN_lib
        python -c "from tl2_lib.tl2.proj.pytorch.examples.gan_ddp.test_gan_ddp import Testing_gan_ddp;\
          Testing_gan_ddp().test_train(debug=False)" \
          --tl_opts root_obs s3://$bucket/ZhouPeng/       \
            use_amp_D False use_amp_G False \
            del_fid_real_images True num_images_real_eval 2048 num_images_gen_eval 2048 \
            save_every 1000 \
          --tl_outdir results/gan_ddp/train-20211129_164456_187

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '1'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'
    if 'RUN_NUM' not in os.environ:
      os.environ['RUN_NUM'] = '0'
    from tl2 import tl2_utils
    from tl2.launch.launch_utils import \
      (get_command_and_outdir, setup_outdir_and_yaml, get_append_cmd_str, start_cmd_run)

    tl_opts_list = tl2_utils.parser_args_from_list(name="--tl_opts", argv_list=sys.argv, type='list')
    tl_opts = ' '.join(tl_opts_list)
    print(f'tl_opts:\n {tl_opts}')

    if debug:
      # sys.argv.extend(['--tl_outdir', 'results/gan_ddp/train-20211129_164456_187'])
      pass
    command, outdir = get_command_and_outdir(self, func_name=sys._getframe().f_code.co_name, file=__file__)
    resume = os.path.isdir(f"{outdir}/ckptdir/resume") and \
             tl2_utils.parser_args_from_list(name="--tl_outdir", argv_list=sys.argv, type='str') is not None
    argv_str = f"""
                --tl_config_file tl2_lib/tl2/proj/pytorch/examples/gan_ddp/config.yaml
                --tl_command {command}
                --tl_outdir {outdir}
                {"--tl_resume --tl_resumedir " + outdir if resume else ""}
                --tl_opts {tl_opts}
                """
    args, cfg = setup_outdir_and_yaml(argv_str, return_cfg=True)

    if int(os.environ['RUN_NUM']) > 0:
      run_command = f"""
                      python -c "from tl2.modelarts.tests.test_run import TestingRun;\
                            TestingRun().test_run_v2(number={os.environ['RUN_NUM']}, )" \
                            --tl_opts root_obs {cfg.root_obs}
                      """
      p = tl2_utils.Worker(name='Run', args=(run_command,))
      p.start()

    os.environ['PATH'] = f"{os.path.dirname(sys.executable)}:{os.environ['PATH']}"
    os.environ['TORCH_EXTENSIONS_DIR'] = "torch_extensions"

    n_gpus = len(os.environ['CUDA_VISIBLE_DEVICES'].split(','))
    PORT = os.environ.get('PORT', 8888)

    cmd_str = f"""
        python
        tl2_lib/tl2/proj/pytorch/examples/gan_ddp/train.py
        --port {PORT}
        --modelarts True
        --outdir {outdir}
        {get_append_cmd_str(args)}
        """
    if debug:
      cmd_str += f"""
                  --tl_debug
                  --tl_opts 
                    num_workers 0                    
                    num_images_real_eval 10
                    num_images_gen_eval 2
                  """
    else:
      cmd_str += f"""
                  --tl_opts {tl_opts}
                    num_workers {n_gpus}
                  """
    start_cmd_run(cmd_str)
    # from tl2.launch.launch_utils import update_parser_defaults_from_yaml, global_cfg
    # from tl2.modelarts import modelarts_utils
    # update_parser_defaults_from_yaml(parser)

    # modelarts_utils.setup_tl_outdir_obs(global_cfg)
    # modelarts_utils.modelarts_sync_results_dir(global_cfg, join=True)
    # modelarts_utils.prepare_dataset(global_cfg.get('modelarts_download', {}), global_cfg=global_cfg)
    #
    # modelarts_utils.prepare_dataset(global_cfg.get('modelarts_upload', {}), global_cfg=global_cfg, download=False)
    # modelarts_utils.modelarts_sync_results_dir(global_cfg, join=True)
    pass


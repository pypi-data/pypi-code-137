# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

"""Custom replacement for `torch.nn.functional.grid_sample` that
supports arbitrarily high order gradients between the input and output.
Only works on 2D images and assumes
`mode='bilinear'`, `padding_mode='zeros'`, `align_corners=False`."""

import torch
from pkg_resources import parse_version

# pylint: disable=redefined-builtin
# pylint: disable=arguments-differ
# pylint: disable=protected-access

# ----------------------------------------------------------------------------

enabled = True  # Enable the custom op by setting this to true.
_use_pytorch_1_11_api = parse_version(torch.__version__) >= parse_version('1.11.0a')  # Allow prerelease builds of 1.11


# ----------------------------------------------------------------------------

def grid_sample(input,
                grid):
  """
  https://github.com/NVlabs/stylegan3/blob/407db86e6fe432540a22515310188288687858fa/torch_utils/ops/grid_sample_gradfix.py
  
  :param input:
  :param grid:
  :return:
  """
  if _should_use_custom_op():
    return _GridSample2dForward.apply(input, grid)
  return torch.nn.functional.grid_sample(input=input, grid=grid, mode='bilinear', padding_mode='zeros',
                                         align_corners=False)


# ----------------------------------------------------------------------------

def _should_use_custom_op():
  return enabled


# ----------------------------------------------------------------------------

class _GridSample2dForward(torch.autograd.Function):
  @staticmethod
  def forward(ctx, input, grid):
    assert input.ndim == 4
    assert grid.ndim == 4
    output = torch.nn.functional.grid_sample(input=input, grid=grid, mode='bilinear', padding_mode='zeros',
                                             align_corners=False)
    ctx.save_for_backward(input, grid)
    return output
  
  @staticmethod
  def backward(ctx, grad_output):
    input, grid = ctx.saved_tensors
    grad_input, grad_grid = _GridSample2dBackward.apply(grad_output, input, grid)
    return grad_input, grad_grid


# ----------------------------------------------------------------------------

class _GridSample2dBackward(torch.autograd.Function):
  @staticmethod
  def forward(ctx, grad_output, input, grid):
    op = torch._C._jit_get_operation('aten::grid_sampler_2d_backward')
    if _use_pytorch_1_11_api:
      output_mask = (ctx.needs_input_grad[1], ctx.needs_input_grad[2])
      grad_input, grad_grid = op(grad_output, input, grid, 0, 0, False, output_mask)
    else:
      grad_input, grad_grid = op(grad_output, input, grid, 0, 0, False)
    ctx.save_for_backward(grid)
    return grad_input, grad_grid
  
  @staticmethod
  def backward(ctx, grad2_grad_input, grad2_grad_grid):
    _ = grad2_grad_grid  # unused
    grid, = ctx.saved_tensors
    grad2_grad_output = None
    grad2_input = None
    grad2_grid = None
    
    if ctx.needs_input_grad[0]:
      grad2_grad_output = _GridSample2dForward.apply(grad2_grad_input, grid)
    
    assert not ctx.needs_input_grad[2]
    return grad2_grad_output, grad2_input, grad2_grid

# ----------------------------------------------------------------------------

if __name__ == '__main__':
  import torch.nn.functional as F
  
  # image = torch.Tensor([[1, 2, 3],
  #                       [4, 5, 6],
  #                       [7, 8, 9]]).view(1, 3, 1, 3)
  image = torch.randn(1, 3, 64, 64)
  
  optical = torch.Tensor([0.9, 0.5, 0.6, -0.7]).view(1, 1, 2, 2)
  
  out = grid_sample(image, optical)
  
  out1 = F.grid_sample(image, optical, padding_mode='zeros', align_corners=False)
  
  err = (out - out1).abs().sum()
  pass
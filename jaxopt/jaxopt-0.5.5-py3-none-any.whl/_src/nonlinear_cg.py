# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Nonlinear conjugate gradient algorithm"""

from typing import Any
from typing import Callable
from typing import NamedTuple
from typing import Optional

from dataclasses import dataclass

import jax
import jax.numpy as jnp

from jaxopt._src import base
from jaxopt._src.backtracking_linesearch import BacktrackingLineSearch
from jaxopt._src.zoom_linesearch import zoom_linesearch
from jaxopt.tree_util import tree_vdot
from jaxopt.tree_util import tree_scalar_mul
from jaxopt.tree_util import tree_add_scalar_mul
from jaxopt.tree_util import tree_sub
from jaxopt.tree_util import tree_div
from jaxopt.tree_util import tree_l2_norm


class NonlinearCGState(NamedTuple):
  """Named tuple containing state information."""
  iter_num: int
  stepsize: float
  error: float
  value: float
  grad: Any
  descent_direction: Any
  aux: Optional[Any] = None


@dataclass(eq=False)
class NonlinearCG(base.IterativeSolver):
  """Nonlinear conjugate gradient solver.

  Attributes:
    fun: a smooth function of the form ``fun(x, *args, **kwargs)``.
    value_and_grad: whether ``fun`` just returns the value (False) or both
      the value and gradient (True).
    has_aux: whether ``fun`` outputs auxiliary data or not.
      If ``value_and_grad == False``, the output should be
      ``value, aux = fun(...)``.
      If ``value_and_grad == True``, the output should be
      ``(value, aux), grad = fun(...)``.
      The auxiliary outputs are stored in ``state.aux``.

    maxiter: maximum number of proximal gradient descent iterations.
    tol: tolerance of the stopping criterion.

    method: which variant to calculate the beta parameter in Nonlinear CG.
      "polak-ribiere", "fletcher-reeves", "hestenes-stiefel"
      (default: "polak-ribiere")

    linesearch: the type of line search to use: "backtracking" for backtracking
      line search or "zoom" for zoom line search.
    maxls: maximum number of iterations to use in the line search.
    decrease_factor: factor by which to decrease the stepsize during line search
      (default: 0.8).
    increase_factor: factor by which to increase the stepsize during line search
      (default: 1.2).
    max_stepsize: upper bound on stepsize.
    min_stepsize: lower bound on stepsize.

    implicit_diff: whether to enable implicit diff or autodiff of unrolled
      iterations.
    implicit_diff_solve: the linear system solver to use.
    jit: whether to JIT-compile the optimization loop (default: "auto").
    unroll: whether to unroll the optimization loop (default: "auto").
    verbose: whether to print error on every iteration or not.
      Warning: verbose=True will automatically disable jit.
  Reference:
    Jorge Nocedal and Stephen Wright.
    Numerical Optimization, second edition.
    Algorithm 5.4 (page 121).
  """

  fun: Callable
  value_and_grad: bool = False
  has_aux: bool = False

  maxiter: int = 100
  tol: float = 1e-3

  method: str = "polak-ribiere"  # same as SciPy
  linesearch: str = "zoom"
  condition: str = "strong-wolfe"
  maxls: int = 15
  decrease_factor: float = 0.8
  increase_factor: float = 1.2
  max_stepsize: float = 1.0
  # FIXME: should depend on whether float32 or float64 is used.
  min_stepsize: float = 1e-6

  implicit_diff: bool = True
  implicit_diff_solve: Optional[Callable] = None

  jit: base.AutoOrBoolean = "auto"
  unroll: base.AutoOrBoolean = "auto"

  verbose: int = 0

  def init_state(self,
                 init_params: Any,
                 *args,
                 **kwargs) -> NonlinearCGState:
    """Initialize the solver state.
    Args:
      init_params: pytree containing the initial parameters.
      *args: additional positional arguments to be passed to ``fun``.
      **kwargs: additional keyword arguments to be passed to ``fun``.
    Returns:
      state
    """
    (value, aux), grad = self._value_and_grad_with_aux(init_params,
                                                       *args,
                                                       **kwargs)

    return NonlinearCGState(iter_num=jnp.asarray(0),
                            stepsize=jnp.asarray(self.max_stepsize),
                            error=jnp.asarray(jnp.inf),
                            value=value,
                            grad=grad,
                            descent_direction=tree_scalar_mul(-1.0, grad),
                            aux=aux)

  def update(self,
             params: Any,
             state: NonlinearCGState,
             *args,
             **kwargs) -> base.OptStep:
    """Performs one iteration of Fletcher-Reeves Algorithm.
    Args:
      params: pytree containing the parameters.
      state: named tuple containing the solver state.
      *args: additional positional arguments to be passed to ``fun``.
      **kwargs: additional keyword arguments to be passed to ``fun``.
    Returns:
      (params, state)
    """

    eps = 1e-6
    value = state.value
    grad = state.grad
    descent_direction = state.descent_direction

    if self.linesearch == "backtracking":
      ls = BacktrackingLineSearch(fun=self._value_and_grad_fun,
                                  value_and_grad=True,
                                  maxiter=self.maxls,
                                  decrease_factor=self.decrease_factor,
                                  condition=self.condition,
                                  max_stepsize=self.max_stepsize)

      init_stepsize = jnp.where(state.stepsize <= self.min_stepsize,
                                # If stepsize became too small, we restart it.
                                self.max_stepsize,
                                # Otherwise, we increase a bit the previous one.
                                state.stepsize * self.increase_factor)

      new_stepsize, ls_state = ls.run(init_stepsize,
                                      params,
                                      value,
                                      grad,
                                      None, # descent_direction
                                      *args, **kwargs)

    elif self.linesearch == "zoom":
      ls_state = zoom_linesearch(f=self._value_and_grad_with_aux,
                                 xk=params, pk=descent_direction,
                                 old_fval=value, gfk=grad, maxiter=self.maxls,
                                 value_and_grad=True, has_aux=True,
                                 args=args, kwargs=kwargs)
      new_stepsize = ls_state.a_k

    else:
      raise ValueError("Invalid name in 'linesearch' option.")

    new_params = tree_add_scalar_mul(params, new_stepsize, descent_direction)
    (new_value, new_aux), new_grad = self._value_and_grad_with_aux(new_params,
                                                                   *args,
                                                                   **kwargs)

    if self.method == "polak-ribiere":
      # See Numerical Optimization, second edition, equation (5.44).
      gTg = tree_vdot(grad, grad)
      gTg = jnp.where(gTg >= eps, gTg, eps)
      new_beta = tree_div(tree_vdot(new_grad, tree_sub(new_grad, grad)), gTg)
      new_beta = jax.nn.relu(new_beta)
    elif self.method == "fletcher-reeves":
      # See Numerical Optimization, second edition, equation (5.41a).
      gTg = tree_vdot(grad, grad)
      gTg = jnp.where(gTg >= eps, gTg, eps)
      new_beta = tree_div(tree_vdot(new_grad, new_grad), gTg)
    elif self.method == 'hestenes-stiefel':
      # See Numerical Optimization, second edition, equation (5.45).
      grad_diff = tree_sub(new_grad, grad)
      dTg = tree_vdot(descent_direction, grad_diff)
      dTg = jnp.where(dTg >= eps, dTg, eps)
      new_beta = tree_div(tree_vdot(new_grad, grad_diff), dTg)
    else:
      raise ValueError("method argument should be either 'polak-ribiere', "
                       "'fletcher-reeves', or 'hestenes-stiefel'.")

    new_descent_direction = tree_add_scalar_mul(tree_scalar_mul(-1, new_grad),
                                                new_beta,
                                                descent_direction)
    new_state = NonlinearCGState(iter_num=state.iter_num + 1,
                                 stepsize=jnp.asarray(new_stepsize),
                                 error=tree_l2_norm(grad),
                                 value=new_value,
                                 grad=new_grad,
                                 descent_direction=new_descent_direction,
                                 aux=new_aux)

    return base.OptStep(params=new_params, state=new_state)

  def optimality_fun(self, params, *args, **kwargs):
    """Optimality function mapping compatible with ``@custom_root``."""
    return self._grad_fun(params, *args, **kwargs)

  def _value_and_grad_fun(self, params, *args, **kwargs):
    (value, aux), grad = self._value_and_grad_with_aux(params, *args, **kwargs)
    return value, grad

  def _grad_fun(self, params, *args, **kwargs):
    return self._value_and_grad_fun(params, *args, **kwargs)[1]

  def __post_init__(self):
    _, _, self._value_and_grad_with_aux = \
      base._make_funs_with_aux(fun=self.fun,
                               value_and_grad=self.value_and_grad,
                               has_aux=self.has_aux)

    self.reference_signature = self.fun

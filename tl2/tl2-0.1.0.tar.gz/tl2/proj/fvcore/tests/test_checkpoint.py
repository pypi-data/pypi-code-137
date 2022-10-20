# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

import copy
import os
import random
import string
import typing
import unittest
from collections import OrderedDict
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock

import torch
from torch import nn

from fvcore.common.checkpoint import PeriodicCheckpointer

from tl2.proj.fvcore.checkpoint import Checkpointer


class TestCheckpointer(unittest.TestCase):
    def _create_model(self) -> nn.Module:
        """
        Create a simple model.
        """
        return nn.Sequential(nn.Linear(2, 3), nn.Linear(3, 1))

    def _create_complex_model(
        self,
    ) -> typing.Tuple[nn.Module, typing.Dict[str, torch.Tensor]]:
        """
        Create a complex model.
        """
        m = nn.Module()
        m.block1 = nn.Module()
        m.block1.layer1 = nn.Linear(2, 3)
        m.layer2 = nn.Linear(3, 2)
        m.res = nn.Module()
        m.res.layer2 = nn.Linear(3, 2)

        state_dict = OrderedDict()
        state_dict["layer1.weight"] = torch.rand(3, 2)
        state_dict["layer1.bias"] = torch.rand(3)
        state_dict["layer2.weight"] = torch.rand(2, 3)
        state_dict["layer2.bias"] = torch.rand(2)
        state_dict["res.layer2.weight"] = torch.rand(2, 3)
        state_dict["res.layer2.bias"] = torch.rand(2)

        return m, state_dict

    def test_loading_objects_with_expected_shape_mismatches(self) -> None:

        m1 = nn.Sequential(nn.Conv2d(2, 2, 1))
        m2 = nn.Sequential(nn.Conv2d(2, 2, 3))

        m1(torch.randn(4, 2, 4, 4))
        # Load m1's checkpoint into m2.
        with TemporaryDirectory() as f:
            checkpointer = Checkpointer(m1, save_dir=f)
            checkpointer.save("checkpoint_file")

            # in the same folder
            fresh_checkpointer = Checkpointer(m2, save_dir=f)
            self.assertTrue(fresh_checkpointer.has_checkpoint())
            self.assertEqual(
                fresh_checkpointer.get_checkpoint_file(),
                os.path.join(f, "checkpoint_file.pth"),
            )
            fresh_checkpointer.load(fresh_checkpointer.get_checkpoint_file())
            pass

    def test_from_last_checkpoint_model(self) -> None:
        """
        test that loading works even if they differ by a prefix.
        """
        for trained_model, fresh_model in [
            (self._create_model(), self._create_model()),
            (nn.DataParallel(self._create_model()), self._create_model()),
            (self._create_model(), nn.DataParallel(self._create_model())),
            (
                nn.DataParallel(self._create_model()),
                nn.DataParallel(self._create_model()),
            ),
        ]:

            with TemporaryDirectory() as f:
                checkpointer = Checkpointer(trained_model, save_dir=f)
                checkpointer.save("checkpoint_file")

                # in the same folder
                fresh_checkpointer = Checkpointer(fresh_model, save_dir=f)
                self.assertTrue(fresh_checkpointer.has_checkpoint())
                self.assertEqual(
                    fresh_checkpointer.get_checkpoint_file(),
                    os.path.join(f, "checkpoint_file.pth"),
                )
                fresh_checkpointer.load(fresh_checkpointer.get_checkpoint_file())

            for trained_p, loaded_p in zip(
                trained_model.parameters(), fresh_model.parameters()
            ):
                # different tensor references
                self.assertFalse(id(trained_p) == id(loaded_p))
                # same content
                self.assertTrue(trained_p.cpu().equal(loaded_p.cpu()))
        pass

    def test_from_name_file_model(self) -> None:
        """
        test that loading works even if they differ by a prefix.
        """
        for trained_model, fresh_model in [
            (self._create_model(), self._create_model()),
            (nn.DataParallel(self._create_model()), self._create_model()),
            (self._create_model(), nn.DataParallel(self._create_model())),
            (
                nn.DataParallel(self._create_model()),
                nn.DataParallel(self._create_model()),
            ),
        ]:
            with TemporaryDirectory() as f:
                checkpointer = Checkpointer(
                    trained_model, save_dir=f, save_to_disk=True
                )
                checkpointer.save("checkpoint_file")

                # on different folders.
                with TemporaryDirectory() as g:
                    fresh_checkpointer = Checkpointer(fresh_model, save_dir=g)
                    self.assertFalse(fresh_checkpointer.has_checkpoint())
                    self.assertEqual(fresh_checkpointer.get_checkpoint_file(), "")
                    fresh_checkpointer.load(os.path.join(f, "checkpoint_file.pth"))

            for trained_p, loaded_p in zip(
                trained_model.parameters(), fresh_model.parameters()
            ):
                # different tensor references.
                self.assertFalse(id(trained_p) == id(loaded_p))
                # same content.
                self.assertTrue(trained_p.cpu().equal(loaded_p.cpu()))
        pass

    def test_checkpointables(self) -> None:
        """
        Test saving and loading checkpointables.
        """

        class CheckpointableObj:
            """
            A dummy checkpointableObj class with state_dict and load_state_dict
            methods.
            """

            def __init__(self):
                self.state = {
                    self.random_handle(): self.random_handle() for i in range(10)
                }

            def random_handle(self, str_len=100) -> str:
                """
                Generate a random string of fixed length.
                Args:
                    str_len (str): length of the output string.
                Returns:
                    (str): random generated handle.
                """
                letters = string.ascii_uppercase
                return "".join(random.choice(letters) for i in range(str_len))

            def state_dict(self):
                """
                Return the state.
                Returns:
                    (dict): return the state.
                """
                return self.state

            def load_state_dict(self, state) -> None:
                """
                Load the state from a given state.
                Args:
                    state (dict): a key value dictionary.
                """
                self.state = copy.deepcopy(state)

        trained_model, fresh_model = self._create_model(), self._create_model()
        with TemporaryDirectory() as f:
            checkpointables = CheckpointableObj()
            checkpointer = Checkpointer(
                trained_model,
                save_dir=f,
                save_to_disk=True,
                checkpointables=checkpointables
            )
            checkpointer.save("checkpoint_file", epoch=0, itr=0)
            # in the same folder
            fresh_checkpointer = Checkpointer(fresh_model, save_dir=f)
            self.assertTrue(fresh_checkpointer.has_checkpoint())
            self.assertEqual(
                fresh_checkpointer.get_checkpoint_file(),
                os.path.join(f, "checkpoint_file.pth"),
            )
            checkpoint = fresh_checkpointer.load(
                fresh_checkpointer.get_checkpoint_file()
            )
            state_dict = checkpointables.state_dict()
            for key, _ in state_dict.items():
                self.assertTrue(checkpoint["checkpointables"].get(key) is not None)
                self.assertTrue(checkpoint["checkpointables"][key] == state_dict[key])
        pass

    def test_load_reused_params(self) -> None:
        class Model(nn.Module):
            def __init__(self, has_y: bool) -> None:
                super().__init__()
                self.x = nn.Linear(10, 10)
                if has_y:
                    self.y = self.x

        model = Model(has_y=False)
        model.x.bias.data.fill_(5.0)  # pyre-ignore
        data = {"model": model.state_dict()}
        new_model = Model(has_y=True)
        chkpt = Checkpointer(new_model)
        # chkpt.logger = logger = MagicMock()
        incompatible = chkpt._load_model(data)
        chkpt._log_incompatible_keys(incompatible)
        self.assertTrue(
            torch.allclose(new_model.y.bias - 5.0, torch.zeros_like(new_model.y.bias))
        )
        # logger.info.assert_not_called()
        pass

    @unittest.skipIf(  # pyre-fixme[56]
        not hasattr(nn, "LazyLinear"), "LazyModule not supported"
    )
    def test_load_lazy_module(self) -> None:
        def _get_model() -> nn.Sequential:  # pyre-fixme[11]
            return nn.Sequential(nn.LazyLinear(10))

        m1, m2 = _get_model(), _get_model()
        m1(torch.randn(4, 2, 4, 4))  # initialize m1, but not m2
        # Load m1's checkpoint into m2.
        with TemporaryDirectory() as f:
            checkpointer = Checkpointer(m1, save_dir=f)
            checkpointer.save("checkpoint_file")

            fresh_checkpointer = Checkpointer(m2, save_dir=f)
            self.assertTrue(fresh_checkpointer.has_checkpoint())
            self.assertEqual(
                fresh_checkpointer.get_checkpoint_file(),
                os.path.join(f, "checkpoint_file.pth"),
            )
            checkpointer.load(fresh_checkpointer.get_checkpoint_file())
            # fresh_checkpointer.load(fresh_checkpointer.get_checkpoint_file())
            self.assertTrue(torch.equal(m1[0].weight, m2[0].weight))
        pass


class TestPeriodicCheckpointer(unittest.TestCase):
    def _create_model(self) -> nn.Module:
        """
        Create a simple model.
        """
        return nn.Sequential(nn.Linear(2, 3), nn.Linear(3, 1))

    def test_periodic_checkpointer(self) -> None:
        """
        test that loading works even if they differ by a prefix.
        """
        _period = 10
        _max_iter = 100
        for trained_model in [
            self._create_model(),
            nn.DataParallel(self._create_model()),
        ]:
            with TemporaryDirectory() as f:
                checkpointer = Checkpointer(
                    trained_model, save_dir=f, save_to_disk=True
                )
                periodic_checkpointer = PeriodicCheckpointer(checkpointer, _period, 99)
                for iteration in range(_max_iter):
                    periodic_checkpointer.step(iteration)
                    path = os.path.join(f, "model_{:07d}.pth".format(iteration))
                    if (iteration + 1) % _period == 0:
                        self.assertTrue(os.path.exists(path))
                    else:
                        self.assertFalse(os.path.exists(path))
        pass

    def test_periodic_checkpointer_max_to_keep(self) -> None:
        """
        Test parameter: max_to_keep
        """
        _period = 10
        _max_iter = 100
        _max_to_keep = 3
        for trained_model in [
            self._create_model(),
            nn.DataParallel(self._create_model()),
        ]:
            with TemporaryDirectory() as f:
                checkpointer = Checkpointer(
                    trained_model, save_dir=f, save_to_disk=True
                )
                periodic_checkpointer = PeriodicCheckpointer(
                    checkpointer, _period, 99, max_to_keep=_max_to_keep
                )
                for _ in range(2):
                    checkpoint_paths = []

                    for iteration in range(_max_iter):
                        periodic_checkpointer.step(iteration)
                        if (iteration + 1) % _period == 0:
                            path = os.path.join(f, "model_{:07d}.pth".format(iteration))
                            checkpoint_paths.append(path)

                    for path in checkpoint_paths[:-_max_to_keep]:
                        self.assertFalse(os.path.exists(path))

                    for path in checkpoint_paths[-_max_to_keep:]:
                        self.assertTrue(os.path.exists(path))


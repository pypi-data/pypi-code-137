# This file is part of lsst-resources.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from typing import Tuple

__all__ = ("InMemoryResourcePath",)

from ._resourcePath import ResourcePath


class InMemoryResourcePath(ResourcePath):
    """Internal in-memory datastore URI (`mem://`).

    Not used for any real purpose other than indicating that the dataset
    is in memory.
    """

    def exists(self) -> bool:
        """Test for existence and always return False."""
        return True

    def _as_local(self) -> Tuple[str, bool]:
        raise RuntimeError(f"Do not know how to retrieve data for URI '{self}'")

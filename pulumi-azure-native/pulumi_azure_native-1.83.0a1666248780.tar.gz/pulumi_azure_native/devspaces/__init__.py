# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .controller import *
from .get_controller import *
from .list_controller_connection_details import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.devspaces.v20190401 as __v20190401
    v20190401 = __v20190401
else:
    v20190401 = _utilities.lazy_import('pulumi_azure_native.devspaces.v20190401')


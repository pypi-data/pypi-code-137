# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .address_by_name import *
from .get_address_by_name import *
from .get_order_item_by_name import *
from .list_configurations import *
from .list_product_families import *
from .order_item_by_name import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.edgeorder.v20201201preview as __v20201201preview
    v20201201preview = __v20201201preview
    import pulumi_azure_native.edgeorder.v20211201 as __v20211201
    v20211201 = __v20211201
    import pulumi_azure_native.edgeorder.v20220501preview as __v20220501preview
    v20220501preview = __v20220501preview
else:
    v20201201preview = _utilities.lazy_import('pulumi_azure_native.edgeorder.v20201201preview')
    v20211201 = _utilities.lazy_import('pulumi_azure_native.edgeorder.v20211201')
    v20220501preview = _utilities.lazy_import('pulumi_azure_native.edgeorder.v20220501preview')


# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AliasPathType
from ._models_py3 import AliasType
from ._models_py3 import BasicDependency
from ._models_py3 import DebugSetting
from ._models_py3 import Dependency
from ._models_py3 import Deployment
from ._models_py3 import DeploymentExportResult
from ._models_py3 import DeploymentExtended
from ._models_py3 import DeploymentExtendedFilter
from ._models_py3 import DeploymentListResult
from ._models_py3 import DeploymentOperation
from ._models_py3 import DeploymentOperationProperties
from ._models_py3 import DeploymentOperationsListResult
from ._models_py3 import DeploymentProperties
from ._models_py3 import DeploymentPropertiesExtended
from ._models_py3 import DeploymentValidateResult
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorResponse
from ._models_py3 import ExportTemplateRequest
from ._models_py3 import GenericResource
from ._models_py3 import GenericResourceExpanded
from ._models_py3 import GenericResourceFilter
from ._models_py3 import HttpMessage
from ._models_py3 import Identity
from ._models_py3 import ParametersLink
from ._models_py3 import Plan
from ._models_py3 import Provider
from ._models_py3 import ProviderListResult
from ._models_py3 import ProviderResourceType
from ._models_py3 import Resource
from ._models_py3 import ResourceGroup
from ._models_py3 import ResourceGroupExportResult
from ._models_py3 import ResourceGroupFilter
from ._models_py3 import ResourceGroupListResult
from ._models_py3 import ResourceGroupPatchable
from ._models_py3 import ResourceGroupProperties
from ._models_py3 import ResourceListResult
from ._models_py3 import ResourceManagementErrorWithDetails
from ._models_py3 import ResourceProviderOperationDisplayProperties
from ._models_py3 import ResourcesMoveInfo
from ._models_py3 import Sku
from ._models_py3 import SubResource
from ._models_py3 import TagCount
from ._models_py3 import TagDetails
from ._models_py3 import TagValue
from ._models_py3 import TagsListResult
from ._models_py3 import TargetResource
from ._models_py3 import TemplateHashResult
from ._models_py3 import TemplateLink
from ._models_py3 import ZoneMapping

from ._resource_management_client_enums import DeploymentMode
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AliasPathType",
    "AliasType",
    "BasicDependency",
    "DebugSetting",
    "Dependency",
    "Deployment",
    "DeploymentExportResult",
    "DeploymentExtended",
    "DeploymentExtendedFilter",
    "DeploymentListResult",
    "DeploymentOperation",
    "DeploymentOperationProperties",
    "DeploymentOperationsListResult",
    "DeploymentProperties",
    "DeploymentPropertiesExtended",
    "DeploymentValidateResult",
    "ErrorAdditionalInfo",
    "ErrorResponse",
    "ExportTemplateRequest",
    "GenericResource",
    "GenericResourceExpanded",
    "GenericResourceFilter",
    "HttpMessage",
    "Identity",
    "ParametersLink",
    "Plan",
    "Provider",
    "ProviderListResult",
    "ProviderResourceType",
    "Resource",
    "ResourceGroup",
    "ResourceGroupExportResult",
    "ResourceGroupFilter",
    "ResourceGroupListResult",
    "ResourceGroupPatchable",
    "ResourceGroupProperties",
    "ResourceListResult",
    "ResourceManagementErrorWithDetails",
    "ResourceProviderOperationDisplayProperties",
    "ResourcesMoveInfo",
    "Sku",
    "SubResource",
    "TagCount",
    "TagDetails",
    "TagValue",
    "TagsListResult",
    "TargetResource",
    "TemplateHashResult",
    "TemplateLink",
    "ZoneMapping",
    "DeploymentMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()

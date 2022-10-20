# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetEntityAnalyticsResult',
    'AwaitableGetEntityAnalyticsResult',
    'get_entity_analytics',
    'get_entity_analytics_output',
]

@pulumi.output_type
class GetEntityAnalyticsResult:
    """
    Settings with single toggle.
    """
    def __init__(__self__, entity_providers=None, etag=None, id=None, kind=None, name=None, system_data=None, type=None):
        if entity_providers and not isinstance(entity_providers, list):
            raise TypeError("Expected argument 'entity_providers' to be a list")
        pulumi.set(__self__, "entity_providers", entity_providers)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="entityProviders")
    def entity_providers(self) -> Optional[Sequence[str]]:
        """
        The relevant entity providers that are synced
        """
        return pulumi.get(self, "entity_providers")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the setting
        Expected value is 'EntityAnalytics'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetEntityAnalyticsResult(GetEntityAnalyticsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntityAnalyticsResult(
            entity_providers=self.entity_providers,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_entity_analytics(resource_group_name: Optional[str] = None,
                         settings_name: Optional[str] = None,
                         workspace_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntityAnalyticsResult:
    """
    Settings with single toggle.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str settings_name: The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['settingsName'] = settings_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20221001preview:getEntityAnalytics', __args__, opts=opts, typ=GetEntityAnalyticsResult).value

    return AwaitableGetEntityAnalyticsResult(
        entity_providers=__ret__.entity_providers,
        etag=__ret__.etag,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_entity_analytics)
def get_entity_analytics_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                settings_name: Optional[pulumi.Input[str]] = None,
                                workspace_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntityAnalyticsResult]:
    """
    Settings with single toggle.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str settings_name: The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
    :param str workspace_name: The name of the workspace.
    """
    ...

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
    'ListActiveConnectivityConfigurationsResult',
    'AwaitableListActiveConnectivityConfigurationsResult',
    'list_active_connectivity_configurations',
    'list_active_connectivity_configurations_output',
]

@pulumi.output_type
class ListActiveConnectivityConfigurationsResult:
    """
    Result of the request to list active connectivity configurations. It contains a list of active connectivity configurations and a skiptoken to get the next set of results.
    """
    def __init__(__self__, skip_token=None, value=None):
        if skip_token and not isinstance(skip_token, str):
            raise TypeError("Expected argument 'skip_token' to be a str")
        pulumi.set(__self__, "skip_token", skip_token)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[str]:
        """
        When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
        """
        return pulumi.get(self, "skip_token")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ActiveConnectivityConfigurationResponse']]:
        """
        Gets a page of active connectivity configurations.
        """
        return pulumi.get(self, "value")


class AwaitableListActiveConnectivityConfigurationsResult(ListActiveConnectivityConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListActiveConnectivityConfigurationsResult(
            skip_token=self.skip_token,
            value=self.value)


def list_active_connectivity_configurations(network_manager_name: Optional[str] = None,
                                            regions: Optional[Sequence[str]] = None,
                                            resource_group_name: Optional[str] = None,
                                            skip_token: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListActiveConnectivityConfigurationsResult:
    """
    Result of the request to list active connectivity configurations. It contains a list of active connectivity configurations and a skiptoken to get the next set of results.


    :param str network_manager_name: The name of the network manager.
    :param Sequence[str] regions: List of regions.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
    """
    __args__ = dict()
    __args__['networkManagerName'] = network_manager_name
    __args__['regions'] = regions
    __args__['resourceGroupName'] = resource_group_name
    __args__['skipToken'] = skip_token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20220101:listActiveConnectivityConfigurations', __args__, opts=opts, typ=ListActiveConnectivityConfigurationsResult).value

    return AwaitableListActiveConnectivityConfigurationsResult(
        skip_token=__ret__.skip_token,
        value=__ret__.value)


@_utilities.lift_output_func(list_active_connectivity_configurations)
def list_active_connectivity_configurations_output(network_manager_name: Optional[pulumi.Input[str]] = None,
                                                   regions: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                   skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListActiveConnectivityConfigurationsResult]:
    """
    Result of the request to list active connectivity configurations. It contains a list of active connectivity configurations and a skiptoken to get the next set of results.


    :param str network_manager_name: The name of the network manager.
    :param Sequence[str] regions: List of regions.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
    """
    ...

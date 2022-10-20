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
    'ListLinkerConfigurationsResult',
    'AwaitableListLinkerConfigurationsResult',
    'list_linker_configurations',
    'list_linker_configurations_output',
]

@pulumi.output_type
class ListLinkerConfigurationsResult:
    """
    Configurations for source resource, include appSettings, connectionString and serviceBindings
    """
    def __init__(__self__, configurations=None):
        if configurations and not isinstance(configurations, list):
            raise TypeError("Expected argument 'configurations' to be a list")
        pulumi.set(__self__, "configurations", configurations)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence['outputs.SourceConfigurationResponse']]:
        """
        The configuration properties for source resource.
        """
        return pulumi.get(self, "configurations")


class AwaitableListLinkerConfigurationsResult(ListLinkerConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListLinkerConfigurationsResult(
            configurations=self.configurations)


def list_linker_configurations(linker_name: Optional[str] = None,
                               resource_uri: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListLinkerConfigurationsResult:
    """
    Configurations for source resource, include appSettings, connectionString and serviceBindings


    :param str linker_name: The name Linker resource.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    """
    __args__ = dict()
    __args__['linkerName'] = linker_name
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicelinker/v20211101preview:listLinkerConfigurations', __args__, opts=opts, typ=ListLinkerConfigurationsResult).value

    return AwaitableListLinkerConfigurationsResult(
        configurations=__ret__.configurations)


@_utilities.lift_output_func(list_linker_configurations)
def list_linker_configurations_output(linker_name: Optional[pulumi.Input[str]] = None,
                                      resource_uri: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListLinkerConfigurationsResult]:
    """
    Configurations for source resource, include appSettings, connectionString and serviceBindings


    :param str linker_name: The name Linker resource.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    """
    ...

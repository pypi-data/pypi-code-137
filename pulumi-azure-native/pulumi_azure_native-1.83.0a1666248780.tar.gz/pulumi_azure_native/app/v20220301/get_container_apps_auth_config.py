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
    'GetContainerAppsAuthConfigResult',
    'AwaitableGetContainerAppsAuthConfigResult',
    'get_container_apps_auth_config',
    'get_container_apps_auth_config_output',
]

@pulumi.output_type
class GetContainerAppsAuthConfigResult:
    """
    Configuration settings for the Azure ContainerApp Service Authentication / Authorization feature.
    """
    def __init__(__self__, global_validation=None, http_settings=None, id=None, identity_providers=None, login=None, name=None, platform=None, system_data=None, type=None):
        if global_validation and not isinstance(global_validation, dict):
            raise TypeError("Expected argument 'global_validation' to be a dict")
        pulumi.set(__self__, "global_validation", global_validation)
        if http_settings and not isinstance(http_settings, dict):
            raise TypeError("Expected argument 'http_settings' to be a dict")
        pulumi.set(__self__, "http_settings", http_settings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_providers and not isinstance(identity_providers, dict):
            raise TypeError("Expected argument 'identity_providers' to be a dict")
        pulumi.set(__self__, "identity_providers", identity_providers)
        if login and not isinstance(login, dict):
            raise TypeError("Expected argument 'login' to be a dict")
        pulumi.set(__self__, "login", login)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform and not isinstance(platform, dict):
            raise TypeError("Expected argument 'platform' to be a dict")
        pulumi.set(__self__, "platform", platform)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="globalValidation")
    def global_validation(self) -> Optional['outputs.GlobalValidationResponse']:
        """
        The configuration settings that determines the validation flow of users using  Service Authentication/Authorization.
        """
        return pulumi.get(self, "global_validation")

    @property
    @pulumi.getter(name="httpSettings")
    def http_settings(self) -> Optional['outputs.HttpSettingsResponse']:
        """
        The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "http_settings")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityProviders")
    def identity_providers(self) -> Optional['outputs.IdentityProvidersResponse']:
        """
        The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "identity_providers")

    @property
    @pulumi.getter
    def login(self) -> Optional['outputs.LoginResponse']:
        """
        The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> Optional['outputs.AuthPlatformResponse']:
        """
        The configuration settings of the platform of ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "platform")

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


class AwaitableGetContainerAppsAuthConfigResult(GetContainerAppsAuthConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerAppsAuthConfigResult(
            global_validation=self.global_validation,
            http_settings=self.http_settings,
            id=self.id,
            identity_providers=self.identity_providers,
            login=self.login,
            name=self.name,
            platform=self.platform,
            system_data=self.system_data,
            type=self.type)


def get_container_apps_auth_config(auth_config_name: Optional[str] = None,
                                   container_app_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerAppsAuthConfigResult:
    """
    Configuration settings for the Azure ContainerApp Service Authentication / Authorization feature.


    :param str auth_config_name: Name of the Container App AuthConfig.
    :param str container_app_name: Name of the Container App.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['authConfigName'] = auth_config_name
    __args__['containerAppName'] = container_app_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20220301:getContainerAppsAuthConfig', __args__, opts=opts, typ=GetContainerAppsAuthConfigResult).value

    return AwaitableGetContainerAppsAuthConfigResult(
        global_validation=__ret__.global_validation,
        http_settings=__ret__.http_settings,
        id=__ret__.id,
        identity_providers=__ret__.identity_providers,
        login=__ret__.login,
        name=__ret__.name,
        platform=__ret__.platform,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_container_apps_auth_config)
def get_container_apps_auth_config_output(auth_config_name: Optional[pulumi.Input[str]] = None,
                                          container_app_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerAppsAuthConfigResult]:
    """
    Configuration settings for the Azure ContainerApp Service Authentication / Authorization feature.


    :param str auth_config_name: Name of the Container App AuthConfig.
    :param str container_app_name: Name of the Container App.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...

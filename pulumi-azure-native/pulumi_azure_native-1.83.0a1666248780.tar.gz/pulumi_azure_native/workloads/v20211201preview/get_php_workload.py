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
    'GetPhpWorkloadResult',
    'AwaitableGetPhpWorkloadResult',
    'get_php_workload',
    'get_php_workload_output',
]

@pulumi.output_type
class GetPhpWorkloadResult:
    """
    Php workload resource
    """
    def __init__(__self__, admin_user_profile=None, app_location=None, backup_profile=None, cache_profile=None, controller_profile=None, database_profile=None, fileshare_profile=None, id=None, identity=None, kind=None, location=None, managed_resource_group_configuration=None, name=None, network_profile=None, php_profile=None, provisioning_state=None, search_profile=None, site_profile=None, sku=None, system_data=None, tags=None, type=None, web_nodes_profile=None):
        if admin_user_profile and not isinstance(admin_user_profile, dict):
            raise TypeError("Expected argument 'admin_user_profile' to be a dict")
        pulumi.set(__self__, "admin_user_profile", admin_user_profile)
        if app_location and not isinstance(app_location, str):
            raise TypeError("Expected argument 'app_location' to be a str")
        pulumi.set(__self__, "app_location", app_location)
        if backup_profile and not isinstance(backup_profile, dict):
            raise TypeError("Expected argument 'backup_profile' to be a dict")
        pulumi.set(__self__, "backup_profile", backup_profile)
        if cache_profile and not isinstance(cache_profile, dict):
            raise TypeError("Expected argument 'cache_profile' to be a dict")
        pulumi.set(__self__, "cache_profile", cache_profile)
        if controller_profile and not isinstance(controller_profile, dict):
            raise TypeError("Expected argument 'controller_profile' to be a dict")
        pulumi.set(__self__, "controller_profile", controller_profile)
        if database_profile and not isinstance(database_profile, dict):
            raise TypeError("Expected argument 'database_profile' to be a dict")
        pulumi.set(__self__, "database_profile", database_profile)
        if fileshare_profile and not isinstance(fileshare_profile, dict):
            raise TypeError("Expected argument 'fileshare_profile' to be a dict")
        pulumi.set(__self__, "fileshare_profile", fileshare_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration and not isinstance(managed_resource_group_configuration, dict):
            raise TypeError("Expected argument 'managed_resource_group_configuration' to be a dict")
        pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if php_profile and not isinstance(php_profile, dict):
            raise TypeError("Expected argument 'php_profile' to be a dict")
        pulumi.set(__self__, "php_profile", php_profile)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if search_profile and not isinstance(search_profile, dict):
            raise TypeError("Expected argument 'search_profile' to be a dict")
        pulumi.set(__self__, "search_profile", search_profile)
        if site_profile and not isinstance(site_profile, dict):
            raise TypeError("Expected argument 'site_profile' to be a dict")
        pulumi.set(__self__, "site_profile", site_profile)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if web_nodes_profile and not isinstance(web_nodes_profile, dict):
            raise TypeError("Expected argument 'web_nodes_profile' to be a dict")
        pulumi.set(__self__, "web_nodes_profile", web_nodes_profile)

    @property
    @pulumi.getter(name="adminUserProfile")
    def admin_user_profile(self) -> 'outputs.UserProfileResponse':
        """
        Admin user profile used for VM and VMSS
        """
        return pulumi.get(self, "admin_user_profile")

    @property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> str:
        """
        The infra resources for PHP workload will be created in this location
        """
        return pulumi.get(self, "app_location")

    @property
    @pulumi.getter(name="backupProfile")
    def backup_profile(self) -> Optional['outputs.BackupProfileResponse']:
        """
        Backup profile
        """
        return pulumi.get(self, "backup_profile")

    @property
    @pulumi.getter(name="cacheProfile")
    def cache_profile(self) -> Optional['outputs.CacheProfileResponse']:
        """
        Cache profile
        """
        return pulumi.get(self, "cache_profile")

    @property
    @pulumi.getter(name="controllerProfile")
    def controller_profile(self) -> 'outputs.NodeProfileResponse':
        """
        Controller VM profile
        """
        return pulumi.get(self, "controller_profile")

    @property
    @pulumi.getter(name="databaseProfile")
    def database_profile(self) -> 'outputs.DatabaseProfileResponse':
        """
        Database profile
        """
        return pulumi.get(self, "database_profile")

    @property
    @pulumi.getter(name="fileshareProfile")
    def fileshare_profile(self) -> Optional['outputs.FileshareProfileResponse']:
        """
        File share profile
        """
        return pulumi.get(self, "fileshare_profile")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.PhpWorkloadResourceResponseIdentity']:
        """
        Identity for the resource. Currently not supported
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Indicates which kind of php workload this resource represent e.g WordPress
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional['outputs.ManagedRGConfigurationResponse']:
        """
        Managed resource group configuration of the workload
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.NetworkProfileResponse']:
        """
        Network profile
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="phpProfile")
    def php_profile(self) -> Optional['outputs.PhpProfileResponse']:
        """
        PHP profile
        """
        return pulumi.get(self, "php_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Php workload resource provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="searchProfile")
    def search_profile(self) -> Optional['outputs.SearchProfileResponse']:
        """
        Search profile
        """
        return pulumi.get(self, "search_profile")

    @property
    @pulumi.getter(name="siteProfile")
    def site_profile(self) -> Optional['outputs.SiteProfileResponse']:
        """
        Site profile
        """
        return pulumi.get(self, "site_profile")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Php workloads SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="webNodesProfile")
    def web_nodes_profile(self) -> 'outputs.VmssNodesProfileResponse':
        """
        VMSS web nodes profile
        """
        return pulumi.get(self, "web_nodes_profile")


class AwaitableGetPhpWorkloadResult(GetPhpWorkloadResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPhpWorkloadResult(
            admin_user_profile=self.admin_user_profile,
            app_location=self.app_location,
            backup_profile=self.backup_profile,
            cache_profile=self.cache_profile,
            controller_profile=self.controller_profile,
            database_profile=self.database_profile,
            fileshare_profile=self.fileshare_profile,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            managed_resource_group_configuration=self.managed_resource_group_configuration,
            name=self.name,
            network_profile=self.network_profile,
            php_profile=self.php_profile,
            provisioning_state=self.provisioning_state,
            search_profile=self.search_profile,
            site_profile=self.site_profile,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            web_nodes_profile=self.web_nodes_profile)


def get_php_workload(php_workload_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPhpWorkloadResult:
    """
    Php workload resource


    :param str php_workload_name: Php workload name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['phpWorkloadName'] = php_workload_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads/v20211201preview:getPhpWorkload', __args__, opts=opts, typ=GetPhpWorkloadResult).value

    return AwaitableGetPhpWorkloadResult(
        admin_user_profile=__ret__.admin_user_profile,
        app_location=__ret__.app_location,
        backup_profile=__ret__.backup_profile,
        cache_profile=__ret__.cache_profile,
        controller_profile=__ret__.controller_profile,
        database_profile=__ret__.database_profile,
        fileshare_profile=__ret__.fileshare_profile,
        id=__ret__.id,
        identity=__ret__.identity,
        kind=__ret__.kind,
        location=__ret__.location,
        managed_resource_group_configuration=__ret__.managed_resource_group_configuration,
        name=__ret__.name,
        network_profile=__ret__.network_profile,
        php_profile=__ret__.php_profile,
        provisioning_state=__ret__.provisioning_state,
        search_profile=__ret__.search_profile,
        site_profile=__ret__.site_profile,
        sku=__ret__.sku,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        web_nodes_profile=__ret__.web_nodes_profile)


@_utilities.lift_output_func(get_php_workload)
def get_php_workload_output(php_workload_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPhpWorkloadResult]:
    """
    Php workload resource


    :param str php_workload_name: Php workload name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...

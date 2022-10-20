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
from ._enums import *
from ._inputs import *

__all__ = ['ManagedClusterArgs', 'ManagedCluster']

@pulumi.input_type
class ManagedClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 aad_profile: Optional[pulumi.Input['ManagedClusterAADProfileArgs']] = None,
                 addon_profiles: Optional[pulumi.Input[Mapping[str, pulumi.Input['ManagedClusterAddonProfileArgs']]]] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedClusterAgentPoolProfileArgs']]]] = None,
                 api_server_authorized_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_prefix: Optional[pulumi.Input[str]] = None,
                 enable_pod_security_policy: Optional[pulumi.Input[bool]] = None,
                 enable_rbac: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input['ManagedClusterIdentityArgs']] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 linux_profile: Optional[pulumi.Input['ContainerServiceLinuxProfileArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['ContainerServiceNetworkProfileArgs']] = None,
                 node_resource_group: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 service_principal_profile: Optional[pulumi.Input['ManagedClusterServicePrincipalProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 windows_profile: Optional[pulumi.Input['ManagedClusterWindowsProfileArgs']] = None):
        """
        The set of arguments for constructing a ManagedCluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['ManagedClusterAADProfileArgs'] aad_profile: Profile of Azure Active Directory configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input['ManagedClusterAddonProfileArgs']]] addon_profiles: Profile of managed cluster add-on.
        :param pulumi.Input[Sequence[pulumi.Input['ManagedClusterAgentPoolProfileArgs']]] agent_pool_profiles: Properties of the agent pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_server_authorized_ip_ranges: (PREVIEW) Authorized IP Ranges to kubernetes API server.
        :param pulumi.Input[str] dns_prefix: DNS prefix specified when creating the managed cluster.
        :param pulumi.Input[bool] enable_pod_security_policy: (DEPRECATING) Whether to enable Kubernetes pod security policy (preview). This feature is set for removal on October 15th, 2020. Learn more at aka.ms/aks/azpodpolicy.
        :param pulumi.Input[bool] enable_rbac: Whether to enable Kubernetes Role-Based Access Control.
        :param pulumi.Input['ManagedClusterIdentityArgs'] identity: The identity of the managed cluster, if configured.
        :param pulumi.Input[str] kubernetes_version: Version of Kubernetes specified when creating the managed cluster.
        :param pulumi.Input['ContainerServiceLinuxProfileArgs'] linux_profile: Profile for Linux VMs in the container service cluster.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['ContainerServiceNetworkProfileArgs'] network_profile: Profile of network configuration.
        :param pulumi.Input[str] node_resource_group: Name of the resource group containing agent pool nodes.
        :param pulumi.Input[str] resource_name: The name of the managed cluster resource.
        :param pulumi.Input['ManagedClusterServicePrincipalProfileArgs'] service_principal_profile: Information about a service principal identity for the cluster to use for manipulating Azure APIs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input['ManagedClusterWindowsProfileArgs'] windows_profile: Profile for Windows VMs in the container service cluster.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if aad_profile is not None:
            pulumi.set(__self__, "aad_profile", aad_profile)
        if addon_profiles is not None:
            pulumi.set(__self__, "addon_profiles", addon_profiles)
        if agent_pool_profiles is not None:
            pulumi.set(__self__, "agent_pool_profiles", agent_pool_profiles)
        if api_server_authorized_ip_ranges is not None:
            pulumi.set(__self__, "api_server_authorized_ip_ranges", api_server_authorized_ip_ranges)
        if dns_prefix is not None:
            pulumi.set(__self__, "dns_prefix", dns_prefix)
        if enable_pod_security_policy is not None:
            pulumi.set(__self__, "enable_pod_security_policy", enable_pod_security_policy)
        if enable_rbac is not None:
            pulumi.set(__self__, "enable_rbac", enable_rbac)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if kubernetes_version is not None:
            pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if linux_profile is not None:
            pulumi.set(__self__, "linux_profile", linux_profile)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if node_resource_group is not None:
            pulumi.set(__self__, "node_resource_group", node_resource_group)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if service_principal_profile is not None:
            pulumi.set(__self__, "service_principal_profile", service_principal_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if windows_profile is not None:
            pulumi.set(__self__, "windows_profile", windows_profile)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional[pulumi.Input['ManagedClusterAADProfileArgs']]:
        """
        Profile of Azure Active Directory configuration.
        """
        return pulumi.get(self, "aad_profile")

    @aad_profile.setter
    def aad_profile(self, value: Optional[pulumi.Input['ManagedClusterAADProfileArgs']]):
        pulumi.set(self, "aad_profile", value)

    @property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ManagedClusterAddonProfileArgs']]]]:
        """
        Profile of managed cluster add-on.
        """
        return pulumi.get(self, "addon_profiles")

    @addon_profiles.setter
    def addon_profiles(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ManagedClusterAddonProfileArgs']]]]):
        pulumi.set(self, "addon_profiles", value)

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagedClusterAgentPoolProfileArgs']]]]:
        """
        Properties of the agent pool.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @agent_pool_profiles.setter
    def agent_pool_profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedClusterAgentPoolProfileArgs']]]]):
        pulumi.set(self, "agent_pool_profiles", value)

    @property
    @pulumi.getter(name="apiServerAuthorizedIPRanges")
    def api_server_authorized_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        (PREVIEW) Authorized IP Ranges to kubernetes API server.
        """
        return pulumi.get(self, "api_server_authorized_ip_ranges")

    @api_server_authorized_ip_ranges.setter
    def api_server_authorized_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "api_server_authorized_ip_ranges", value)

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        DNS prefix specified when creating the managed cluster.
        """
        return pulumi.get(self, "dns_prefix")

    @dns_prefix.setter
    def dns_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_prefix", value)

    @property
    @pulumi.getter(name="enablePodSecurityPolicy")
    def enable_pod_security_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        (DEPRECATING) Whether to enable Kubernetes pod security policy (preview). This feature is set for removal on October 15th, 2020. Learn more at aka.ms/aks/azpodpolicy.
        """
        return pulumi.get(self, "enable_pod_security_policy")

    @enable_pod_security_policy.setter
    def enable_pod_security_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_pod_security_policy", value)

    @property
    @pulumi.getter(name="enableRBAC")
    def enable_rbac(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable Kubernetes Role-Based Access Control.
        """
        return pulumi.get(self, "enable_rbac")

    @enable_rbac.setter
    def enable_rbac(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_rbac", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedClusterIdentityArgs']]:
        """
        The identity of the managed cluster, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedClusterIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of Kubernetes specified when creating the managed cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_version", value)

    @property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[pulumi.Input['ContainerServiceLinuxProfileArgs']]:
        """
        Profile for Linux VMs in the container service cluster.
        """
        return pulumi.get(self, "linux_profile")

    @linux_profile.setter
    def linux_profile(self, value: Optional[pulumi.Input['ContainerServiceLinuxProfileArgs']]):
        pulumi.set(self, "linux_profile", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['ContainerServiceNetworkProfileArgs']]:
        """
        Profile of network configuration.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['ContainerServiceNetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource group containing agent pool nodes.
        """
        return pulumi.get(self, "node_resource_group")

    @node_resource_group.setter
    def node_resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_resource_group", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(self) -> Optional[pulumi.Input['ManagedClusterServicePrincipalProfileArgs']]:
        """
        Information about a service principal identity for the cluster to use for manipulating Azure APIs.
        """
        return pulumi.get(self, "service_principal_profile")

    @service_principal_profile.setter
    def service_principal_profile(self, value: Optional[pulumi.Input['ManagedClusterServicePrincipalProfileArgs']]):
        pulumi.set(self, "service_principal_profile", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> Optional[pulumi.Input['ManagedClusterWindowsProfileArgs']]:
        """
        Profile for Windows VMs in the container service cluster.
        """
        return pulumi.get(self, "windows_profile")

    @windows_profile.setter
    def windows_profile(self, value: Optional[pulumi.Input['ManagedClusterWindowsProfileArgs']]):
        pulumi.set(self, "windows_profile", value)


warnings.warn("""Version 2019-04-01 will be removed in v2 of the provider.""", DeprecationWarning)


class ManagedCluster(pulumi.CustomResource):
    warnings.warn("""Version 2019-04-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_profile: Optional[pulumi.Input[pulumi.InputType['ManagedClusterAADProfileArgs']]] = None,
                 addon_profiles: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ManagedClusterAddonProfileArgs']]]]] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedClusterAgentPoolProfileArgs']]]]] = None,
                 api_server_authorized_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_prefix: Optional[pulumi.Input[str]] = None,
                 enable_pod_security_policy: Optional[pulumi.Input[bool]] = None,
                 enable_rbac: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedClusterIdentityArgs']]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 linux_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceLinuxProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceNetworkProfileArgs']]] = None,
                 node_resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 service_principal_profile: Optional[pulumi.Input[pulumi.InputType['ManagedClusterServicePrincipalProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 windows_profile: Optional[pulumi.Input[pulumi.InputType['ManagedClusterWindowsProfileArgs']]] = None,
                 __props__=None):
        """
        Managed cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ManagedClusterAADProfileArgs']] aad_profile: Profile of Azure Active Directory configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ManagedClusterAddonProfileArgs']]]] addon_profiles: Profile of managed cluster add-on.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedClusterAgentPoolProfileArgs']]]] agent_pool_profiles: Properties of the agent pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_server_authorized_ip_ranges: (PREVIEW) Authorized IP Ranges to kubernetes API server.
        :param pulumi.Input[str] dns_prefix: DNS prefix specified when creating the managed cluster.
        :param pulumi.Input[bool] enable_pod_security_policy: (DEPRECATING) Whether to enable Kubernetes pod security policy (preview). This feature is set for removal on October 15th, 2020. Learn more at aka.ms/aks/azpodpolicy.
        :param pulumi.Input[bool] enable_rbac: Whether to enable Kubernetes Role-Based Access Control.
        :param pulumi.Input[pulumi.InputType['ManagedClusterIdentityArgs']] identity: The identity of the managed cluster, if configured.
        :param pulumi.Input[str] kubernetes_version: Version of Kubernetes specified when creating the managed cluster.
        :param pulumi.Input[pulumi.InputType['ContainerServiceLinuxProfileArgs']] linux_profile: Profile for Linux VMs in the container service cluster.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['ContainerServiceNetworkProfileArgs']] network_profile: Profile of network configuration.
        :param pulumi.Input[str] node_resource_group: Name of the resource group containing agent pool nodes.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_name_: The name of the managed cluster resource.
        :param pulumi.Input[pulumi.InputType['ManagedClusterServicePrincipalProfileArgs']] service_principal_profile: Information about a service principal identity for the cluster to use for manipulating Azure APIs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[pulumi.InputType['ManagedClusterWindowsProfileArgs']] windows_profile: Profile for Windows VMs in the container service cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Managed cluster.

        :param str resource_name: The name of the resource.
        :param ManagedClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_profile: Optional[pulumi.Input[pulumi.InputType['ManagedClusterAADProfileArgs']]] = None,
                 addon_profiles: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ManagedClusterAddonProfileArgs']]]]] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedClusterAgentPoolProfileArgs']]]]] = None,
                 api_server_authorized_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_prefix: Optional[pulumi.Input[str]] = None,
                 enable_pod_security_policy: Optional[pulumi.Input[bool]] = None,
                 enable_rbac: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedClusterIdentityArgs']]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 linux_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceLinuxProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceNetworkProfileArgs']]] = None,
                 node_resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 service_principal_profile: Optional[pulumi.Input[pulumi.InputType['ManagedClusterServicePrincipalProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 windows_profile: Optional[pulumi.Input[pulumi.InputType['ManagedClusterWindowsProfileArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ManagedCluster is deprecated: Version 2019-04-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedClusterArgs.__new__(ManagedClusterArgs)

            __props__.__dict__["aad_profile"] = aad_profile
            __props__.__dict__["addon_profiles"] = addon_profiles
            __props__.__dict__["agent_pool_profiles"] = agent_pool_profiles
            __props__.__dict__["api_server_authorized_ip_ranges"] = api_server_authorized_ip_ranges
            __props__.__dict__["dns_prefix"] = dns_prefix
            __props__.__dict__["enable_pod_security_policy"] = enable_pod_security_policy
            __props__.__dict__["enable_rbac"] = enable_rbac
            __props__.__dict__["identity"] = identity
            __props__.__dict__["kubernetes_version"] = kubernetes_version
            __props__.__dict__["linux_profile"] = linux_profile
            __props__.__dict__["location"] = location
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["node_resource_group"] = node_resource_group
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["service_principal_profile"] = service_principal_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["windows_profile"] = windows_profile
            __props__.__dict__["fqdn"] = None
            __props__.__dict__["max_agent_pools"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20170831:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20180331:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20180801preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190601:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190801:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20191001:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20191101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200301:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200401:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200601:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200701:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200901:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20201101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20201201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210301:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210501:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210701:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210801:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210901:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20211001:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20211101preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220102preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220202preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220301:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220302preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220401:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220402preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220502preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220601:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220602preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220701:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220702preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220802preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220803preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20220902preview:ManagedCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedCluster, __self__).__init__(
            'azure-native:containerservice/v20190401:ManagedCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedCluster':
        """
        Get an existing ManagedCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedClusterArgs.__new__(ManagedClusterArgs)

        __props__.__dict__["aad_profile"] = None
        __props__.__dict__["addon_profiles"] = None
        __props__.__dict__["agent_pool_profiles"] = None
        __props__.__dict__["api_server_authorized_ip_ranges"] = None
        __props__.__dict__["dns_prefix"] = None
        __props__.__dict__["enable_pod_security_policy"] = None
        __props__.__dict__["enable_rbac"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["linux_profile"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_agent_pools"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["node_resource_group"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_principal_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["windows_profile"] = None
        return ManagedCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> pulumi.Output[Optional['outputs.ManagedClusterAADProfileResponse']]:
        """
        Profile of Azure Active Directory configuration.
        """
        return pulumi.get(self, "aad_profile")

    @property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ManagedClusterAddonProfileResponse']]]:
        """
        Profile of managed cluster add-on.
        """
        return pulumi.get(self, "addon_profiles")

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> pulumi.Output[Optional[Sequence['outputs.ManagedClusterAgentPoolProfileResponse']]]:
        """
        Properties of the agent pool.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @property
    @pulumi.getter(name="apiServerAuthorizedIPRanges")
    def api_server_authorized_ip_ranges(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        (PREVIEW) Authorized IP Ranges to kubernetes API server.
        """
        return pulumi.get(self, "api_server_authorized_ip_ranges")

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        DNS prefix specified when creating the managed cluster.
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter(name="enablePodSecurityPolicy")
    def enable_pod_security_policy(self) -> pulumi.Output[Optional[bool]]:
        """
        (DEPRECATING) Whether to enable Kubernetes pod security policy (preview). This feature is set for removal on October 15th, 2020. Learn more at aka.ms/aks/azpodpolicy.
        """
        return pulumi.get(self, "enable_pod_security_policy")

    @property
    @pulumi.getter(name="enableRBAC")
    def enable_rbac(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable Kubernetes Role-Based Access Control.
        """
        return pulumi.get(self, "enable_rbac")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        FQDN for the master pool.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedClusterIdentityResponse']]:
        """
        The identity of the managed cluster, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[Optional[str]]:
        """
        Version of Kubernetes specified when creating the managed cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> pulumi.Output[Optional['outputs.ContainerServiceLinuxProfileResponse']]:
        """
        Profile for Linux VMs in the container service cluster.
        """
        return pulumi.get(self, "linux_profile")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxAgentPools")
    def max_agent_pools(self) -> pulumi.Output[int]:
        """
        The max number of agent pools for the managed cluster.
        """
        return pulumi.get(self, "max_agent_pools")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.ContainerServiceNetworkProfileResponse']]:
        """
        Profile of network configuration.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the resource group containing agent pool nodes.
        """
        return pulumi.get(self, "node_resource_group")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(self) -> pulumi.Output[Optional['outputs.ManagedClusterServicePrincipalProfileResponse']]:
        """
        Information about a service principal identity for the cluster to use for manipulating Azure APIs.
        """
        return pulumi.get(self, "service_principal_profile")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> pulumi.Output[Optional['outputs.ManagedClusterWindowsProfileResponse']]:
        """
        Profile for Windows VMs in the container service cluster.
        """
        return pulumi.get(self, "windows_profile")


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
    'GetAFDCustomDomainResult',
    'AwaitableGetAFDCustomDomainResult',
    'get_afd_custom_domain',
    'get_afd_custom_domain_output',
]

@pulumi.output_type
class GetAFDCustomDomainResult:
    """
    Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.
    """
    def __init__(__self__, azure_dns_zone=None, deployment_status=None, domain_validation_state=None, extended_properties=None, host_name=None, id=None, name=None, pre_validated_custom_domain_resource_id=None, profile_name=None, provisioning_state=None, system_data=None, tls_settings=None, type=None, validation_properties=None):
        if azure_dns_zone and not isinstance(azure_dns_zone, dict):
            raise TypeError("Expected argument 'azure_dns_zone' to be a dict")
        pulumi.set(__self__, "azure_dns_zone", azure_dns_zone)
        if deployment_status and not isinstance(deployment_status, str):
            raise TypeError("Expected argument 'deployment_status' to be a str")
        pulumi.set(__self__, "deployment_status", deployment_status)
        if domain_validation_state and not isinstance(domain_validation_state, str):
            raise TypeError("Expected argument 'domain_validation_state' to be a str")
        pulumi.set(__self__, "domain_validation_state", domain_validation_state)
        if extended_properties and not isinstance(extended_properties, dict):
            raise TypeError("Expected argument 'extended_properties' to be a dict")
        pulumi.set(__self__, "extended_properties", extended_properties)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pre_validated_custom_domain_resource_id and not isinstance(pre_validated_custom_domain_resource_id, dict):
            raise TypeError("Expected argument 'pre_validated_custom_domain_resource_id' to be a dict")
        pulumi.set(__self__, "pre_validated_custom_domain_resource_id", pre_validated_custom_domain_resource_id)
        if profile_name and not isinstance(profile_name, str):
            raise TypeError("Expected argument 'profile_name' to be a str")
        pulumi.set(__self__, "profile_name", profile_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tls_settings and not isinstance(tls_settings, dict):
            raise TypeError("Expected argument 'tls_settings' to be a dict")
        pulumi.set(__self__, "tls_settings", tls_settings)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if validation_properties and not isinstance(validation_properties, dict):
            raise TypeError("Expected argument 'validation_properties' to be a dict")
        pulumi.set(__self__, "validation_properties", validation_properties)

    @property
    @pulumi.getter(name="azureDnsZone")
    def azure_dns_zone(self) -> Optional['outputs.ResourceReferenceResponse']:
        """
        Resource reference to the Azure DNS zone
        """
        return pulumi.get(self, "azure_dns_zone")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> str:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="domainValidationState")
    def domain_validation_state(self) -> str:
        """
        Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. DCV stands for DomainControlValidation.
        """
        return pulumi.get(self, "domain_validation_state")

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[Mapping[str, str]]:
        """
        Key-Value pair representing migration properties for domains.
        """
        return pulumi.get(self, "extended_properties")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The host name of the domain. Must be a domain name.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preValidatedCustomDomainResourceId")
    def pre_validated_custom_domain_resource_id(self) -> Optional['outputs.ResourceReferenceResponse']:
        """
        Resource reference to the Azure resource where custom domain ownership was prevalidated
        """
        return pulumi.get(self, "pre_validated_custom_domain_resource_id")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> str:
        """
        The name of the profile which holds the domain.
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Optional['outputs.AFDDomainHttpsParametersResponse']:
        """
        The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.
        """
        return pulumi.get(self, "tls_settings")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationProperties")
    def validation_properties(self) -> 'outputs.DomainValidationPropertiesResponse':
        """
        Values the customer needs to validate domain ownership
        """
        return pulumi.get(self, "validation_properties")


class AwaitableGetAFDCustomDomainResult(GetAFDCustomDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAFDCustomDomainResult(
            azure_dns_zone=self.azure_dns_zone,
            deployment_status=self.deployment_status,
            domain_validation_state=self.domain_validation_state,
            extended_properties=self.extended_properties,
            host_name=self.host_name,
            id=self.id,
            name=self.name,
            pre_validated_custom_domain_resource_id=self.pre_validated_custom_domain_resource_id,
            profile_name=self.profile_name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tls_settings=self.tls_settings,
            type=self.type,
            validation_properties=self.validation_properties)


def get_afd_custom_domain(custom_domain_name: Optional[str] = None,
                          profile_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAFDCustomDomainResult:
    """
    Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.


    :param str custom_domain_name: Name of the domain under the profile which is unique globally.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['customDomainName'] = custom_domain_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cdn/v20220501preview:getAFDCustomDomain', __args__, opts=opts, typ=GetAFDCustomDomainResult).value

    return AwaitableGetAFDCustomDomainResult(
        azure_dns_zone=__ret__.azure_dns_zone,
        deployment_status=__ret__.deployment_status,
        domain_validation_state=__ret__.domain_validation_state,
        extended_properties=__ret__.extended_properties,
        host_name=__ret__.host_name,
        id=__ret__.id,
        name=__ret__.name,
        pre_validated_custom_domain_resource_id=__ret__.pre_validated_custom_domain_resource_id,
        profile_name=__ret__.profile_name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tls_settings=__ret__.tls_settings,
        type=__ret__.type,
        validation_properties=__ret__.validation_properties)


@_utilities.lift_output_func(get_afd_custom_domain)
def get_afd_custom_domain_output(custom_domain_name: Optional[pulumi.Input[str]] = None,
                                 profile_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAFDCustomDomainResult]:
    """
    Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.


    :param str custom_domain_name: Name of the domain under the profile which is unique globally.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...

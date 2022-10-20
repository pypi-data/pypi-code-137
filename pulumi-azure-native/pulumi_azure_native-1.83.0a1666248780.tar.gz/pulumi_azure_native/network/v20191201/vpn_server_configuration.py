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

__all__ = ['VpnServerConfigurationArgs', 'VpnServerConfiguration']

@pulumi.input_type
class VpnServerConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 aad_authentication_parameters: Optional[pulumi.Input['AadAuthenticationParametersArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 radius_client_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusClientRootCertificateArgs']]]] = None,
                 radius_server_address: Optional[pulumi.Input[str]] = None,
                 radius_server_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusServerRootCertificateArgs']]]] = None,
                 radius_server_secret: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpn_authentication_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]]] = None,
                 vpn_client_ipsec_policies: Optional[pulumi.Input[Sequence[pulumi.Input['IpsecPolicyArgs']]]] = None,
                 vpn_client_revoked_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRevokedCertificateArgs']]]] = None,
                 vpn_client_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRootCertificateArgs']]]] = None,
                 vpn_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]]] = None,
                 vpn_server_configuration_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpnServerConfiguration resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VpnServerConfiguration.
        :param pulumi.Input['AadAuthenticationParametersArgs'] aad_authentication_parameters: The set of aad vpn authentication parameters.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] name: The name of the VpnServerConfiguration that is unique within a resource group.
        :param pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusClientRootCertificateArgs']]] radius_client_root_certificates: Radius client root certificate of VpnServerConfiguration.
        :param pulumi.Input[str] radius_server_address: The radius server address property of the VpnServerConfiguration resource for point to site client connection.
        :param pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusServerRootCertificateArgs']]] radius_server_root_certificates: Radius Server root certificate of VpnServerConfiguration.
        :param pulumi.Input[str] radius_server_secret: The radius secret property of the VpnServerConfiguration resource for point to site client connection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]] vpn_authentication_types: VPN authentication types for the VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input['IpsecPolicyArgs']]] vpn_client_ipsec_policies: VpnClientIpsecPolicies for VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRevokedCertificateArgs']]] vpn_client_revoked_certificates: VPN client revoked certificate of VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRootCertificateArgs']]] vpn_client_root_certificates: VPN client root certificate of VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]] vpn_protocols: VPN protocols for the VpnServerConfiguration.
        :param pulumi.Input[str] vpn_server_configuration_name: The name of the VpnServerConfiguration being created or updated.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if aad_authentication_parameters is not None:
            pulumi.set(__self__, "aad_authentication_parameters", aad_authentication_parameters)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if radius_client_root_certificates is not None:
            pulumi.set(__self__, "radius_client_root_certificates", radius_client_root_certificates)
        if radius_server_address is not None:
            pulumi.set(__self__, "radius_server_address", radius_server_address)
        if radius_server_root_certificates is not None:
            pulumi.set(__self__, "radius_server_root_certificates", radius_server_root_certificates)
        if radius_server_secret is not None:
            pulumi.set(__self__, "radius_server_secret", radius_server_secret)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpn_authentication_types is not None:
            pulumi.set(__self__, "vpn_authentication_types", vpn_authentication_types)
        if vpn_client_ipsec_policies is not None:
            pulumi.set(__self__, "vpn_client_ipsec_policies", vpn_client_ipsec_policies)
        if vpn_client_revoked_certificates is not None:
            pulumi.set(__self__, "vpn_client_revoked_certificates", vpn_client_revoked_certificates)
        if vpn_client_root_certificates is not None:
            pulumi.set(__self__, "vpn_client_root_certificates", vpn_client_root_certificates)
        if vpn_protocols is not None:
            pulumi.set(__self__, "vpn_protocols", vpn_protocols)
        if vpn_server_configuration_name is not None:
            pulumi.set(__self__, "vpn_server_configuration_name", vpn_server_configuration_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the VpnServerConfiguration.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="aadAuthenticationParameters")
    def aad_authentication_parameters(self) -> Optional[pulumi.Input['AadAuthenticationParametersArgs']]:
        """
        The set of aad vpn authentication parameters.
        """
        return pulumi.get(self, "aad_authentication_parameters")

    @aad_authentication_parameters.setter
    def aad_authentication_parameters(self, value: Optional[pulumi.Input['AadAuthenticationParametersArgs']]):
        pulumi.set(self, "aad_authentication_parameters", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VpnServerConfiguration that is unique within a resource group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="radiusClientRootCertificates")
    def radius_client_root_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusClientRootCertificateArgs']]]]:
        """
        Radius client root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_client_root_certificates")

    @radius_client_root_certificates.setter
    def radius_client_root_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusClientRootCertificateArgs']]]]):
        pulumi.set(self, "radius_client_root_certificates", value)

    @property
    @pulumi.getter(name="radiusServerAddress")
    def radius_server_address(self) -> Optional[pulumi.Input[str]]:
        """
        The radius server address property of the VpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_address")

    @radius_server_address.setter
    def radius_server_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "radius_server_address", value)

    @property
    @pulumi.getter(name="radiusServerRootCertificates")
    def radius_server_root_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusServerRootCertificateArgs']]]]:
        """
        Radius Server root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_server_root_certificates")

    @radius_server_root_certificates.setter
    def radius_server_root_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigRadiusServerRootCertificateArgs']]]]):
        pulumi.set(self, "radius_server_root_certificates", value)

    @property
    @pulumi.getter(name="radiusServerSecret")
    def radius_server_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The radius secret property of the VpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_secret")

    @radius_server_secret.setter
    def radius_server_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "radius_server_secret", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpnAuthenticationTypes")
    def vpn_authentication_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]]]:
        """
        VPN authentication types for the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_authentication_types")

    @vpn_authentication_types.setter
    def vpn_authentication_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]]]):
        pulumi.set(self, "vpn_authentication_types", value)

    @property
    @pulumi.getter(name="vpnClientIpsecPolicies")
    def vpn_client_ipsec_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpsecPolicyArgs']]]]:
        """
        VpnClientIpsecPolicies for VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_ipsec_policies")

    @vpn_client_ipsec_policies.setter
    def vpn_client_ipsec_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpsecPolicyArgs']]]]):
        pulumi.set(self, "vpn_client_ipsec_policies", value)

    @property
    @pulumi.getter(name="vpnClientRevokedCertificates")
    def vpn_client_revoked_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRevokedCertificateArgs']]]]:
        """
        VPN client revoked certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_revoked_certificates")

    @vpn_client_revoked_certificates.setter
    def vpn_client_revoked_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRevokedCertificateArgs']]]]):
        pulumi.set(self, "vpn_client_revoked_certificates", value)

    @property
    @pulumi.getter(name="vpnClientRootCertificates")
    def vpn_client_root_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRootCertificateArgs']]]]:
        """
        VPN client root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_root_certificates")

    @vpn_client_root_certificates.setter
    def vpn_client_root_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigVpnClientRootCertificateArgs']]]]):
        pulumi.set(self, "vpn_client_root_certificates", value)

    @property
    @pulumi.getter(name="vpnProtocols")
    def vpn_protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]]]:
        """
        VPN protocols for the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_protocols")

    @vpn_protocols.setter
    def vpn_protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]]]):
        pulumi.set(self, "vpn_protocols", value)

    @property
    @pulumi.getter(name="vpnServerConfigurationName")
    def vpn_server_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VpnServerConfiguration being created or updated.
        """
        return pulumi.get(self, "vpn_server_configuration_name")

    @vpn_server_configuration_name.setter
    def vpn_server_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpn_server_configuration_name", value)


class VpnServerConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_authentication_parameters: Optional[pulumi.Input[pulumi.InputType['AadAuthenticationParametersArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 radius_client_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigRadiusClientRootCertificateArgs']]]]] = None,
                 radius_server_address: Optional[pulumi.Input[str]] = None,
                 radius_server_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigRadiusServerRootCertificateArgs']]]]] = None,
                 radius_server_secret: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpn_authentication_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]]] = None,
                 vpn_client_ipsec_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpsecPolicyArgs']]]]] = None,
                 vpn_client_revoked_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigVpnClientRevokedCertificateArgs']]]]] = None,
                 vpn_client_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigVpnClientRootCertificateArgs']]]]] = None,
                 vpn_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]]] = None,
                 vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        VpnServerConfiguration Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AadAuthenticationParametersArgs']] aad_authentication_parameters: The set of aad vpn authentication parameters.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] name: The name of the VpnServerConfiguration that is unique within a resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigRadiusClientRootCertificateArgs']]]] radius_client_root_certificates: Radius client root certificate of VpnServerConfiguration.
        :param pulumi.Input[str] radius_server_address: The radius server address property of the VpnServerConfiguration resource for point to site client connection.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigRadiusServerRootCertificateArgs']]]] radius_server_root_certificates: Radius Server root certificate of VpnServerConfiguration.
        :param pulumi.Input[str] radius_server_secret: The radius secret property of the VpnServerConfiguration resource for point to site client connection.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VpnServerConfiguration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]] vpn_authentication_types: VPN authentication types for the VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpsecPolicyArgs']]]] vpn_client_ipsec_policies: VpnClientIpsecPolicies for VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigVpnClientRevokedCertificateArgs']]]] vpn_client_revoked_certificates: VPN client revoked certificate of VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigVpnClientRootCertificateArgs']]]] vpn_client_root_certificates: VPN client root certificate of VpnServerConfiguration.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]] vpn_protocols: VPN protocols for the VpnServerConfiguration.
        :param pulumi.Input[str] vpn_server_configuration_name: The name of the VpnServerConfiguration being created or updated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnServerConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VpnServerConfiguration Resource.

        :param str resource_name: The name of the resource.
        :param VpnServerConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnServerConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_authentication_parameters: Optional[pulumi.Input[pulumi.InputType['AadAuthenticationParametersArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 radius_client_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigRadiusClientRootCertificateArgs']]]]] = None,
                 radius_server_address: Optional[pulumi.Input[str]] = None,
                 radius_server_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigRadiusServerRootCertificateArgs']]]]] = None,
                 radius_server_secret: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpn_authentication_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnAuthenticationType']]]]] = None,
                 vpn_client_ipsec_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpsecPolicyArgs']]]]] = None,
                 vpn_client_revoked_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigVpnClientRevokedCertificateArgs']]]]] = None,
                 vpn_client_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnServerConfigVpnClientRootCertificateArgs']]]]] = None,
                 vpn_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'VpnGatewayTunnelingProtocol']]]]] = None,
                 vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnServerConfigurationArgs.__new__(VpnServerConfigurationArgs)

            __props__.__dict__["aad_authentication_parameters"] = aad_authentication_parameters
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["radius_client_root_certificates"] = radius_client_root_certificates
            __props__.__dict__["radius_server_address"] = radius_server_address
            __props__.__dict__["radius_server_root_certificates"] = radius_server_root_certificates
            __props__.__dict__["radius_server_secret"] = radius_server_secret
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpn_authentication_types"] = vpn_authentication_types
            __props__.__dict__["vpn_client_ipsec_policies"] = vpn_client_ipsec_policies
            __props__.__dict__["vpn_client_revoked_certificates"] = vpn_client_revoked_certificates
            __props__.__dict__["vpn_client_root_certificates"] = vpn_client_root_certificates
            __props__.__dict__["vpn_protocols"] = vpn_protocols
            __props__.__dict__["vpn_server_configuration_name"] = vpn_server_configuration_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["p2_s_vpn_gateways"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20190801:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20190901:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20191101:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20200301:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20200401:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20200501:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20200601:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20200701:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20200801:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20201101:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20210201:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20210301:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20210501:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20210801:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20220101:VpnServerConfiguration"), pulumi.Alias(type_="azure-native:network/v20220501:VpnServerConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VpnServerConfiguration, __self__).__init__(
            'azure-native:network/v20191201:VpnServerConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpnServerConfiguration':
        """
        Get an existing VpnServerConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpnServerConfigurationArgs.__new__(VpnServerConfigurationArgs)

        __props__.__dict__["aad_authentication_parameters"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["p2_s_vpn_gateways"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["radius_client_root_certificates"] = None
        __props__.__dict__["radius_server_address"] = None
        __props__.__dict__["radius_server_root_certificates"] = None
        __props__.__dict__["radius_server_secret"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vpn_authentication_types"] = None
        __props__.__dict__["vpn_client_ipsec_policies"] = None
        __props__.__dict__["vpn_client_revoked_certificates"] = None
        __props__.__dict__["vpn_client_root_certificates"] = None
        __props__.__dict__["vpn_protocols"] = None
        return VpnServerConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aadAuthenticationParameters")
    def aad_authentication_parameters(self) -> pulumi.Output[Optional['outputs.AadAuthenticationParametersResponse']]:
        """
        The set of aad vpn authentication parameters.
        """
        return pulumi.get(self, "aad_authentication_parameters")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SVpnGateways")
    def p2_s_vpn_gateways(self) -> pulumi.Output[Sequence['outputs.P2SVpnGatewayResponse']]:
        """
        List of references to P2SVpnGateways.
        """
        return pulumi.get(self, "p2_s_vpn_gateways")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the VpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="radiusClientRootCertificates")
    def radius_client_root_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.VpnServerConfigRadiusClientRootCertificateResponse']]]:
        """
        Radius client root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_client_root_certificates")

    @property
    @pulumi.getter(name="radiusServerAddress")
    def radius_server_address(self) -> pulumi.Output[Optional[str]]:
        """
        The radius server address property of the VpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_address")

    @property
    @pulumi.getter(name="radiusServerRootCertificates")
    def radius_server_root_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.VpnServerConfigRadiusServerRootCertificateResponse']]]:
        """
        Radius Server root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_server_root_certificates")

    @property
    @pulumi.getter(name="radiusServerSecret")
    def radius_server_secret(self) -> pulumi.Output[Optional[str]]:
        """
        The radius secret property of the VpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_secret")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vpnAuthenticationTypes")
    def vpn_authentication_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        VPN authentication types for the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_authentication_types")

    @property
    @pulumi.getter(name="vpnClientIpsecPolicies")
    def vpn_client_ipsec_policies(self) -> pulumi.Output[Optional[Sequence['outputs.IpsecPolicyResponse']]]:
        """
        VpnClientIpsecPolicies for VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_ipsec_policies")

    @property
    @pulumi.getter(name="vpnClientRevokedCertificates")
    def vpn_client_revoked_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.VpnServerConfigVpnClientRevokedCertificateResponse']]]:
        """
        VPN client revoked certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_revoked_certificates")

    @property
    @pulumi.getter(name="vpnClientRootCertificates")
    def vpn_client_root_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.VpnServerConfigVpnClientRootCertificateResponse']]]:
        """
        VPN client root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_root_certificates")

    @property
    @pulumi.getter(name="vpnProtocols")
    def vpn_protocols(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        VPN protocols for the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_protocols")


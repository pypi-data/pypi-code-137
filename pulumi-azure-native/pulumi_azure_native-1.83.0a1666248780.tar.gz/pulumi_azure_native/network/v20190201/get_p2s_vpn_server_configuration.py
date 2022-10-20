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
    'GetP2sVpnServerConfigurationResult',
    'AwaitableGetP2sVpnServerConfigurationResult',
    'get_p2s_vpn_server_configuration',
    'get_p2s_vpn_server_configuration_output',
]

@pulumi.output_type
class GetP2sVpnServerConfigurationResult:
    """
    P2SVpnServerConfiguration Resource.
    """
    def __init__(__self__, etag=None, id=None, name=None, p2_s_vpn_gateways=None, p2_s_vpn_server_config_radius_client_root_certificates=None, p2_s_vpn_server_config_radius_server_root_certificates=None, p2_s_vpn_server_config_vpn_client_revoked_certificates=None, p2_s_vpn_server_config_vpn_client_root_certificates=None, provisioning_state=None, radius_server_address=None, radius_server_secret=None, vpn_client_ipsec_policies=None, vpn_protocols=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if p2_s_vpn_gateways and not isinstance(p2_s_vpn_gateways, list):
            raise TypeError("Expected argument 'p2_s_vpn_gateways' to be a list")
        pulumi.set(__self__, "p2_s_vpn_gateways", p2_s_vpn_gateways)
        if p2_s_vpn_server_config_radius_client_root_certificates and not isinstance(p2_s_vpn_server_config_radius_client_root_certificates, list):
            raise TypeError("Expected argument 'p2_s_vpn_server_config_radius_client_root_certificates' to be a list")
        pulumi.set(__self__, "p2_s_vpn_server_config_radius_client_root_certificates", p2_s_vpn_server_config_radius_client_root_certificates)
        if p2_s_vpn_server_config_radius_server_root_certificates and not isinstance(p2_s_vpn_server_config_radius_server_root_certificates, list):
            raise TypeError("Expected argument 'p2_s_vpn_server_config_radius_server_root_certificates' to be a list")
        pulumi.set(__self__, "p2_s_vpn_server_config_radius_server_root_certificates", p2_s_vpn_server_config_radius_server_root_certificates)
        if p2_s_vpn_server_config_vpn_client_revoked_certificates and not isinstance(p2_s_vpn_server_config_vpn_client_revoked_certificates, list):
            raise TypeError("Expected argument 'p2_s_vpn_server_config_vpn_client_revoked_certificates' to be a list")
        pulumi.set(__self__, "p2_s_vpn_server_config_vpn_client_revoked_certificates", p2_s_vpn_server_config_vpn_client_revoked_certificates)
        if p2_s_vpn_server_config_vpn_client_root_certificates and not isinstance(p2_s_vpn_server_config_vpn_client_root_certificates, list):
            raise TypeError("Expected argument 'p2_s_vpn_server_config_vpn_client_root_certificates' to be a list")
        pulumi.set(__self__, "p2_s_vpn_server_config_vpn_client_root_certificates", p2_s_vpn_server_config_vpn_client_root_certificates)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if radius_server_address and not isinstance(radius_server_address, str):
            raise TypeError("Expected argument 'radius_server_address' to be a str")
        pulumi.set(__self__, "radius_server_address", radius_server_address)
        if radius_server_secret and not isinstance(radius_server_secret, str):
            raise TypeError("Expected argument 'radius_server_secret' to be a str")
        pulumi.set(__self__, "radius_server_secret", radius_server_secret)
        if vpn_client_ipsec_policies and not isinstance(vpn_client_ipsec_policies, list):
            raise TypeError("Expected argument 'vpn_client_ipsec_policies' to be a list")
        pulumi.set(__self__, "vpn_client_ipsec_policies", vpn_client_ipsec_policies)
        if vpn_protocols and not isinstance(vpn_protocols, list):
            raise TypeError("Expected argument 'vpn_protocols' to be a list")
        pulumi.set(__self__, "vpn_protocols", vpn_protocols)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the P2SVpnServerConfiguration that is unique within a VirtualWan in a resource group. This name can be used to access the resource along with Paren VirtualWan resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SVpnGateways")
    def p2_s_vpn_gateways(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to P2SVpnGateways.
        """
        return pulumi.get(self, "p2_s_vpn_gateways")

    @property
    @pulumi.getter(name="p2SVpnServerConfigRadiusClientRootCertificates")
    def p2_s_vpn_server_config_radius_client_root_certificates(self) -> Optional[Sequence['outputs.P2SVpnServerConfigRadiusClientRootCertificateResponse']]:
        """
        Radius client root certificate of P2SVpnServerConfiguration.
        """
        return pulumi.get(self, "p2_s_vpn_server_config_radius_client_root_certificates")

    @property
    @pulumi.getter(name="p2SVpnServerConfigRadiusServerRootCertificates")
    def p2_s_vpn_server_config_radius_server_root_certificates(self) -> Optional[Sequence['outputs.P2SVpnServerConfigRadiusServerRootCertificateResponse']]:
        """
        Radius Server root certificate of P2SVpnServerConfiguration.
        """
        return pulumi.get(self, "p2_s_vpn_server_config_radius_server_root_certificates")

    @property
    @pulumi.getter(name="p2SVpnServerConfigVpnClientRevokedCertificates")
    def p2_s_vpn_server_config_vpn_client_revoked_certificates(self) -> Optional[Sequence['outputs.P2SVpnServerConfigVpnClientRevokedCertificateResponse']]:
        """
        VPN client revoked certificate of P2SVpnServerConfiguration.
        """
        return pulumi.get(self, "p2_s_vpn_server_config_vpn_client_revoked_certificates")

    @property
    @pulumi.getter(name="p2SVpnServerConfigVpnClientRootCertificates")
    def p2_s_vpn_server_config_vpn_client_root_certificates(self) -> Optional[Sequence['outputs.P2SVpnServerConfigVpnClientRootCertificateResponse']]:
        """
        VPN client root certificate of P2SVpnServerConfiguration.
        """
        return pulumi.get(self, "p2_s_vpn_server_config_vpn_client_root_certificates")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the P2SVpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="radiusServerAddress")
    def radius_server_address(self) -> Optional[str]:
        """
        The radius server address property of the P2SVpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_address")

    @property
    @pulumi.getter(name="radiusServerSecret")
    def radius_server_secret(self) -> Optional[str]:
        """
        The radius secret property of the P2SVpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_secret")

    @property
    @pulumi.getter(name="vpnClientIpsecPolicies")
    def vpn_client_ipsec_policies(self) -> Optional[Sequence['outputs.IpsecPolicyResponse']]:
        """
        VpnClientIpsecPolicies for P2SVpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_ipsec_policies")

    @property
    @pulumi.getter(name="vpnProtocols")
    def vpn_protocols(self) -> Optional[Sequence[str]]:
        """
        VPN protocols for the P2SVpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_protocols")


class AwaitableGetP2sVpnServerConfigurationResult(GetP2sVpnServerConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetP2sVpnServerConfigurationResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            p2_s_vpn_gateways=self.p2_s_vpn_gateways,
            p2_s_vpn_server_config_radius_client_root_certificates=self.p2_s_vpn_server_config_radius_client_root_certificates,
            p2_s_vpn_server_config_radius_server_root_certificates=self.p2_s_vpn_server_config_radius_server_root_certificates,
            p2_s_vpn_server_config_vpn_client_revoked_certificates=self.p2_s_vpn_server_config_vpn_client_revoked_certificates,
            p2_s_vpn_server_config_vpn_client_root_certificates=self.p2_s_vpn_server_config_vpn_client_root_certificates,
            provisioning_state=self.provisioning_state,
            radius_server_address=self.radius_server_address,
            radius_server_secret=self.radius_server_secret,
            vpn_client_ipsec_policies=self.vpn_client_ipsec_policies,
            vpn_protocols=self.vpn_protocols)


def get_p2s_vpn_server_configuration(p2_s_vpn_server_configuration_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     virtual_wan_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetP2sVpnServerConfigurationResult:
    """
    P2SVpnServerConfiguration Resource.


    :param str p2_s_vpn_server_configuration_name: The name of the P2SVpnServerConfiguration.
    :param str resource_group_name: The resource group name of the P2SVpnServerConfiguration.
    :param str virtual_wan_name: The name of the VirtualWan.
    """
    __args__ = dict()
    __args__['p2SVpnServerConfigurationName'] = p2_s_vpn_server_configuration_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualWanName'] = virtual_wan_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20190201:getP2sVpnServerConfiguration', __args__, opts=opts, typ=GetP2sVpnServerConfigurationResult).value

    return AwaitableGetP2sVpnServerConfigurationResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        p2_s_vpn_gateways=__ret__.p2_s_vpn_gateways,
        p2_s_vpn_server_config_radius_client_root_certificates=__ret__.p2_s_vpn_server_config_radius_client_root_certificates,
        p2_s_vpn_server_config_radius_server_root_certificates=__ret__.p2_s_vpn_server_config_radius_server_root_certificates,
        p2_s_vpn_server_config_vpn_client_revoked_certificates=__ret__.p2_s_vpn_server_config_vpn_client_revoked_certificates,
        p2_s_vpn_server_config_vpn_client_root_certificates=__ret__.p2_s_vpn_server_config_vpn_client_root_certificates,
        provisioning_state=__ret__.provisioning_state,
        radius_server_address=__ret__.radius_server_address,
        radius_server_secret=__ret__.radius_server_secret,
        vpn_client_ipsec_policies=__ret__.vpn_client_ipsec_policies,
        vpn_protocols=__ret__.vpn_protocols)


@_utilities.lift_output_func(get_p2s_vpn_server_configuration)
def get_p2s_vpn_server_configuration_output(p2_s_vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            virtual_wan_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetP2sVpnServerConfigurationResult]:
    """
    P2SVpnServerConfiguration Resource.


    :param str p2_s_vpn_server_configuration_name: The name of the P2SVpnServerConfiguration.
    :param str resource_group_name: The resource group name of the P2SVpnServerConfiguration.
    :param str virtual_wan_name: The name of the VirtualWan.
    """
    ...

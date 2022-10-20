# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Access',
    'ApplicationGatewayCookieBasedAffinity',
    'ApplicationGatewayFirewallMode',
    'ApplicationGatewayProtocol',
    'ApplicationGatewayRedirectType',
    'ApplicationGatewayRequestRoutingRuleType',
    'ApplicationGatewaySkuName',
    'ApplicationGatewaySslCipherSuite',
    'ApplicationGatewaySslPolicyName',
    'ApplicationGatewaySslPolicyType',
    'ApplicationGatewaySslProtocol',
    'ApplicationGatewayTier',
    'AuthorizationUseStatus',
    'AzureFirewallApplicationRuleProtocolType',
    'AzureFirewallNetworkRuleProtocol',
    'AzureFirewallRCActionType',
    'DhGroup',
    'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState',
    'ExpressRouteCircuitPeeringState',
    'ExpressRouteCircuitSkuFamily',
    'ExpressRouteCircuitSkuTier',
    'ExpressRoutePeeringState',
    'ExpressRoutePeeringType',
    'IPAllocationMethod',
    'IPVersion',
    'IkeEncryption',
    'IkeIntegrity',
    'IpsecEncryption',
    'IpsecIntegrity',
    'LoadBalancerSkuName',
    'LoadDistribution',
    'PcProtocol',
    'PfsGroup',
    'ProbeProtocol',
    'PublicIPAddressSkuName',
    'RouteFilterRuleType',
    'RouteNextHopType',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'SecurityRuleProtocol',
    'ServiceProviderProvisioningState',
    'TransportProtocol',
    'VirtualNetworkGatewayConnectionType',
    'VirtualNetworkGatewaySkuName',
    'VirtualNetworkGatewaySkuTier',
    'VirtualNetworkGatewayType',
    'VirtualNetworkPeeringState',
    'VpnClientProtocol',
    'VpnType',
]


class Access(str, Enum):
    """
    The access type of the rule. Valid values are: 'Allow', 'Deny'
    """
    ALLOW = "Allow"
    DENY = "Deny"


class ApplicationGatewayCookieBasedAffinity(str, Enum):
    """
    Cookie based affinity.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ApplicationGatewayFirewallMode(str, Enum):
    """
    Web application firewall mode.
    """
    DETECTION = "Detection"
    PREVENTION = "Prevention"


class ApplicationGatewayProtocol(str, Enum):
    """
    The protocol used for the probe. Possible values are 'Http' and 'Https'.
    """
    HTTP = "Http"
    HTTPS = "Https"


class ApplicationGatewayRedirectType(str, Enum):
    """
    Supported http redirection types - Permanent, Temporary, Found, SeeOther.
    """
    PERMANENT = "Permanent"
    FOUND = "Found"
    SEE_OTHER = "SeeOther"
    TEMPORARY = "Temporary"


class ApplicationGatewayRequestRoutingRuleType(str, Enum):
    """
    Rule type.
    """
    BASIC = "Basic"
    PATH_BASED_ROUTING = "PathBasedRouting"


class ApplicationGatewaySkuName(str, Enum):
    """
    Name of an application gateway SKU.
    """
    STANDARD_SMALL = "Standard_Small"
    STANDARD_MEDIUM = "Standard_Medium"
    STANDARD_LARGE = "Standard_Large"
    WA_F_MEDIUM = "WAF_Medium"
    WA_F_LARGE = "WAF_Large"
    STANDARD_V2 = "Standard_v2"
    WA_F_V2 = "WAF_v2"


class ApplicationGatewaySslCipherSuite(str, Enum):
    """
    Ssl cipher suites enums.
    """
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_256_CB_C_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
    TL_S_DH_E_RS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384"
    TL_S_DH_E_RS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
    TL_S_DH_E_RS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA"
    TL_S_DH_E_RS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA"
    TL_S_RS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_RSA_WITH_AES_256_GCM_SHA384"
    TL_S_RS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_RSA_WITH_AES_128_GCM_SHA256"
    TL_S_RS_A_WIT_H_AE_S_256_CB_C_SHA256 = "TLS_RSA_WITH_AES_256_CBC_SHA256"
    TL_S_RS_A_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_RSA_WITH_AES_128_CBC_SHA256"
    TL_S_RS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_RSA_WITH_AES_256_CBC_SHA"
    TL_S_RS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_RSA_WITH_AES_128_CBC_SHA"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_256_CB_C_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA"
    TL_S_DH_E_DS_S_WIT_H_AE_S_256_CB_C_SHA256 = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256"
    TL_S_DH_E_DS_S_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256"
    TL_S_DH_E_DS_S_WIT_H_AE_S_256_CB_C_SHA = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA"
    TL_S_DH_E_DS_S_WIT_H_AE_S_128_CB_C_SHA = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA"
    TL_S_RS_A_WIT_H_3_DE_S_ED_E_CB_C_SHA = "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
    TL_S_DH_E_DS_S_WIT_H_3_DE_S_ED_E_CB_C_SHA = "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"


class ApplicationGatewaySslPolicyName(str, Enum):
    """
    Name of Ssl predefined policy
    """
    APP_GW_SSL_POLICY20150501 = "AppGwSslPolicy20150501"
    APP_GW_SSL_POLICY20170401 = "AppGwSslPolicy20170401"
    APP_GW_SSL_POLICY20170401_S = "AppGwSslPolicy20170401S"


class ApplicationGatewaySslPolicyType(str, Enum):
    """
    Type of Ssl Policy
    """
    PREDEFINED = "Predefined"
    CUSTOM = "Custom"


class ApplicationGatewaySslProtocol(str, Enum):
    """
    Minimum version of Ssl protocol to be supported on application gateway.
    """
    TL_SV1_0 = "TLSv1_0"
    TL_SV1_1 = "TLSv1_1"
    TL_SV1_2 = "TLSv1_2"


class ApplicationGatewayTier(str, Enum):
    """
    Tier of an application gateway.
    """
    STANDARD = "Standard"
    WAF = "WAF"
    STANDARD_V2 = "Standard_v2"
    WA_F_V2 = "WAF_v2"


class AuthorizationUseStatus(str, Enum):
    """
    AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
    """
    AVAILABLE = "Available"
    IN_USE = "InUse"


class AzureFirewallApplicationRuleProtocolType(str, Enum):
    """
    Protocol type
    """
    HTTP = "Http"
    HTTPS = "Https"


class AzureFirewallNetworkRuleProtocol(str, Enum):
    """
    The protocol of a Network Rule resource
    """
    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class AzureFirewallRCActionType(str, Enum):
    """
    The type of action.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class DhGroup(str, Enum):
    """
    The DH Groups used in IKE Phase 1 for initial SA.
    """
    NONE = "None"
    DH_GROUP1 = "DHGroup1"
    DH_GROUP2 = "DHGroup2"
    DH_GROUP14 = "DHGroup14"
    DH_GROUP2048 = "DHGroup2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    DH_GROUP24 = "DHGroup24"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum):
    """
    AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured', 'Configuring', 'Configured', and 'ValidationNeeded'.
    """
    NOT_CONFIGURED = "NotConfigured"
    CONFIGURING = "Configuring"
    CONFIGURED = "Configured"
    VALIDATION_NEEDED = "ValidationNeeded"


class ExpressRouteCircuitPeeringState(str, Enum):
    """
    The state of peering. Possible values are: 'Disabled' and 'Enabled'
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRouteCircuitSkuFamily(str, Enum):
    """
    The family of the SKU. Possible values are: 'UnlimitedData' and 'MeteredData'.
    """
    UNLIMITED_DATA = "UnlimitedData"
    METERED_DATA = "MeteredData"


class ExpressRouteCircuitSkuTier(str, Enum):
    """
    The tier of the SKU. Possible values are 'Standard' and 'Premium'.
    """
    STANDARD = "Standard"
    PREMIUM = "Premium"


class ExpressRoutePeeringState(str, Enum):
    """
    The peering state.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRoutePeeringType(str, Enum):
    """
    The peering type.
    """
    AZURE_PUBLIC_PEERING = "AzurePublicPeering"
    AZURE_PRIVATE_PEERING = "AzurePrivatePeering"
    MICROSOFT_PEERING = "MicrosoftPeering"


class IPAllocationMethod(str, Enum):
    """
    The private IP allocation method. Possible values are: 'Static' and 'Dynamic'.
    """
    STATIC = "Static"
    DYNAMIC = "Dynamic"


class IPVersion(str, Enum):
    """
    The public IP address version. Possible values are: 'IPv4' and 'IPv6'.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class IkeEncryption(str, Enum):
    """
    The IKE encryption algorithm (IKE phase 2).
    """
    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IkeIntegrity(str, Enum):
    """
    The IKE integrity algorithm (IKE phase 2).
    """
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IpsecEncryption(str, Enum):
    """
    The IPSec encryption algorithm (IKE phase 1).
    """
    NONE = "None"
    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class IpsecIntegrity(str, Enum):
    """
    The IPSec integrity algorithm (IKE phase 1).
    """
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class LoadBalancerSkuName(str, Enum):
    """
    Name of a load balancer SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class LoadDistribution(str, Enum):
    """
    The load distribution policy for this rule. Possible values are 'Default', 'SourceIP', and 'SourceIPProtocol'.
    """
    DEFAULT = "Default"
    SOURCE_IP = "SourceIP"
    SOURCE_IP_PROTOCOL = "SourceIPProtocol"


class PcProtocol(str, Enum):
    """
    Protocol to be filtered on.
    """
    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"


class PfsGroup(str, Enum):
    """
    The Pfs Groups used in IKE Phase 2 for new child SA.
    """
    NONE = "None"
    PFS1 = "PFS1"
    PFS2 = "PFS2"
    PFS2048 = "PFS2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    PFS24 = "PFS24"
    PFS14 = "PFS14"
    PFSMM = "PFSMM"


class ProbeProtocol(str, Enum):
    """
    The protocol of the end point. Possible values are: 'Http', 'Tcp', or 'Https'. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI is required for the probe to be successful.
    """
    HTTP = "Http"
    TCP = "Tcp"
    HTTPS = "Https"


class PublicIPAddressSkuName(str, Enum):
    """
    Name of a public IP address SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class RouteFilterRuleType(str, Enum):
    """
    The rule type of the rule. Valid value is: 'Community'
    """
    COMMUNITY = "Community"


class RouteNextHopType(str, Enum):
    """
    The type of Azure hop the packet should be sent to. Possible values are: 'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance', and 'None'
    """
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    NONE = "None"


class SecurityRuleAccess(str, Enum):
    """
    The network traffic is allowed or denied. Possible values are: 'Allow' and 'Deny'.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class SecurityRuleDirection(str, Enum):
    """
    The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are: 'Inbound' and 'Outbound'.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityRuleProtocol(str, Enum):
    """
    Network protocol this rule applies to. Possible values are 'Tcp', 'Udp', and '*'.
    """
    TCP = "Tcp"
    UDP = "Udp"
    ASTERISK = "*"


class ServiceProviderProvisioningState(str, Enum):
    """
    The ServiceProviderProvisioningState state of the resource. Possible values are 'NotProvisioned', 'Provisioning', 'Provisioned', and 'Deprovisioning'.
    """
    NOT_PROVISIONED = "NotProvisioned"
    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    DEPROVISIONING = "Deprovisioning"


class TransportProtocol(str, Enum):
    """
    The transport protocol for the endpoint. Possible values are 'Udp' or 'Tcp' or 'All'.
    """
    UDP = "Udp"
    TCP = "Tcp"
    ALL = "All"


class VirtualNetworkGatewayConnectionType(str, Enum):
    """
    Gateway connection type. Possible values are: 'IPsec','Vnet2Vnet','ExpressRoute', and 'VPNClient.
    """
    IPSEC = "IPsec"
    VNET2_VNET = "Vnet2Vnet"
    EXPRESS_ROUTE = "ExpressRoute"
    VPN_CLIENT = "VPNClient"


class VirtualNetworkGatewaySkuName(str, Enum):
    """
    Gateway SKU name.
    """
    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"
    VPN_GW1 = "VpnGw1"
    VPN_GW2 = "VpnGw2"
    VPN_GW3 = "VpnGw3"
    VPN_GW1_AZ = "VpnGw1AZ"
    VPN_GW2_AZ = "VpnGw2AZ"
    VPN_GW3_AZ = "VpnGw3AZ"
    ER_GW1_AZ = "ErGw1AZ"
    ER_GW2_AZ = "ErGw2AZ"
    ER_GW3_AZ = "ErGw3AZ"


class VirtualNetworkGatewaySkuTier(str, Enum):
    """
    Gateway SKU tier.
    """
    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"
    VPN_GW1 = "VpnGw1"
    VPN_GW2 = "VpnGw2"
    VPN_GW3 = "VpnGw3"
    VPN_GW1_AZ = "VpnGw1AZ"
    VPN_GW2_AZ = "VpnGw2AZ"
    VPN_GW3_AZ = "VpnGw3AZ"
    ER_GW1_AZ = "ErGw1AZ"
    ER_GW2_AZ = "ErGw2AZ"
    ER_GW3_AZ = "ErGw3AZ"


class VirtualNetworkGatewayType(str, Enum):
    """
    The type of this virtual network gateway. Possible values are: 'Vpn' and 'ExpressRoute'.
    """
    VPN = "Vpn"
    EXPRESS_ROUTE = "ExpressRoute"


class VirtualNetworkPeeringState(str, Enum):
    """
    The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and 'Disconnected'.
    """
    INITIATED = "Initiated"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"


class VpnClientProtocol(str, Enum):
    """
    VPN client protocol enabled for the virtual network gateway.
    """
    IKE_V2 = "IkeV2"
    SSTP = "SSTP"
    OPEN_VPN = "OpenVPN"


class VpnType(str, Enum):
    """
    The type of this virtual network gateway. Possible values are: 'PolicyBased' and 'RouteBased'.
    """
    POLICY_BASED = "PolicyBased"
    ROUTE_BASED = "RouteBased"

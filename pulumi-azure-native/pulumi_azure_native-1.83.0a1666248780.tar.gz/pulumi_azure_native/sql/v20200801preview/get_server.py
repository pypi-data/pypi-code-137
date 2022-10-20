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
    'GetServerResult',
    'AwaitableGetServerResult',
    'get_server',
    'get_server_output',
]

@pulumi.output_type
class GetServerResult:
    """
    An Azure SQL Database server.
    """
    def __init__(__self__, administrator_login=None, fully_qualified_domain_name=None, id=None, identity=None, kind=None, location=None, minimal_tls_version=None, name=None, private_endpoint_connections=None, public_network_access=None, state=None, tags=None, type=None, version=None, workspace_feature=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if fully_qualified_domain_name and not isinstance(fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
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
        if minimal_tls_version and not isinstance(minimal_tls_version, str):
            raise TypeError("Expected argument 'minimal_tls_version' to be a str")
        pulumi.set(__self__, "minimal_tls_version", minimal_tls_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if workspace_feature and not isinstance(workspace_feature, str):
            raise TypeError("Expected argument 'workspace_feature' to be a str")
        pulumi.set(__self__, "workspace_feature", workspace_feature)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[str]:
        """
        Administrator username for the server. Once created it cannot be changed.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of the server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ResourceIdentityResponse']:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of sql server. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[str]:
        """
        Minimal TLS version. Allowed values: '1.0', '1.1', '1.2'
        """
        return pulumi.get(self, "minimal_tls_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.ServerPrivateEndpointConnectionResponse']:
        """
        List of private endpoint connections on a server
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the server.
        """
        return pulumi.get(self, "state")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the server.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="workspaceFeature")
    def workspace_feature(self) -> str:
        """
        Whether or not existing server has a workspace created and if it allows connection from workspace
        """
        return pulumi.get(self, "workspace_feature")


class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            administrator_login=self.administrator_login,
            fully_qualified_domain_name=self.fully_qualified_domain_name,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            minimal_tls_version=self.minimal_tls_version,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            public_network_access=self.public_network_access,
            state=self.state,
            tags=self.tags,
            type=self.type,
            version=self.version,
            workspace_feature=self.workspace_feature)


def get_server(resource_group_name: Optional[str] = None,
               server_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerResult:
    """
    An Azure SQL Database server.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20200801preview:getServer', __args__, opts=opts, typ=GetServerResult).value

    return AwaitableGetServerResult(
        administrator_login=__ret__.administrator_login,
        fully_qualified_domain_name=__ret__.fully_qualified_domain_name,
        id=__ret__.id,
        identity=__ret__.identity,
        kind=__ret__.kind,
        location=__ret__.location,
        minimal_tls_version=__ret__.minimal_tls_version,
        name=__ret__.name,
        private_endpoint_connections=__ret__.private_endpoint_connections,
        public_network_access=__ret__.public_network_access,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type,
        version=__ret__.version,
        workspace_feature=__ret__.workspace_feature)


@_utilities.lift_output_func(get_server)
def get_server_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                      server_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerResult]:
    """
    An Azure SQL Database server.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...

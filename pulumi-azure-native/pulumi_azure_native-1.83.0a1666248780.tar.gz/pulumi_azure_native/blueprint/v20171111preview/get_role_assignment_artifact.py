# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetRoleAssignmentArtifactResult',
    'AwaitableGetRoleAssignmentArtifactResult',
    'get_role_assignment_artifact',
    'get_role_assignment_artifact_output',
]

@pulumi.output_type
class GetRoleAssignmentArtifactResult:
    """
    Blueprint artifact applies Azure role assignment.
    """
    def __init__(__self__, depends_on=None, description=None, display_name=None, id=None, kind=None, name=None, principal_ids=None, resource_group=None, role_definition_id=None, type=None):
        if depends_on and not isinstance(depends_on, list):
            raise TypeError("Expected argument 'depends_on' to be a list")
        pulumi.set(__self__, "depends_on", depends_on)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal_ids and not isinstance(principal_ids, dict):
            raise TypeError("Expected argument 'principal_ids' to be a dict")
        pulumi.set(__self__, "principal_ids", principal_ids)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if role_definition_id and not isinstance(role_definition_id, str):
            raise TypeError("Expected argument 'role_definition_id' to be a str")
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[str]]:
        """
        Artifacts which need to be deployed before the specified artifact.
        """
        return pulumi.get(self, "depends_on")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Specifies the kind of Blueprint artifact.
        Expected value is 'roleAssignment'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalIds")
    def principal_ids(self) -> Any:
        """
        Array of user or group identities in Azure Active Directory. The roleDefinition will apply to these identity.
        """
        return pulumi.get(self, "principal_ids")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[str]:
        """
        RoleAssignment will be scope to this resourceGroup, if left empty, it would scope to the subscription.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> str:
        """
        Azure resource ID of the RoleDefinition.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetRoleAssignmentArtifactResult(GetRoleAssignmentArtifactResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleAssignmentArtifactResult(
            depends_on=self.depends_on,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            kind=self.kind,
            name=self.name,
            principal_ids=self.principal_ids,
            resource_group=self.resource_group,
            role_definition_id=self.role_definition_id,
            type=self.type)


def get_role_assignment_artifact(artifact_name: Optional[str] = None,
                                 blueprint_name: Optional[str] = None,
                                 management_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleAssignmentArtifactResult:
    """
    Blueprint artifact applies Azure role assignment.


    :param str artifact_name: name of the artifact.
    :param str blueprint_name: name of the blueprint.
    :param str management_group_name: ManagementGroup where blueprint stores.
    """
    __args__ = dict()
    __args__['artifactName'] = artifact_name
    __args__['blueprintName'] = blueprint_name
    __args__['managementGroupName'] = management_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:blueprint/v20171111preview:getRoleAssignmentArtifact', __args__, opts=opts, typ=GetRoleAssignmentArtifactResult).value

    return AwaitableGetRoleAssignmentArtifactResult(
        depends_on=__ret__.depends_on,
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        principal_ids=__ret__.principal_ids,
        resource_group=__ret__.resource_group,
        role_definition_id=__ret__.role_definition_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_role_assignment_artifact)
def get_role_assignment_artifact_output(artifact_name: Optional[pulumi.Input[str]] = None,
                                        blueprint_name: Optional[pulumi.Input[str]] = None,
                                        management_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleAssignmentArtifactResult]:
    """
    Blueprint artifact applies Azure role assignment.


    :param str artifact_name: name of the artifact.
    :param str blueprint_name: name of the blueprint.
    :param str management_group_name: ManagementGroup where blueprint stores.
    """
    ...

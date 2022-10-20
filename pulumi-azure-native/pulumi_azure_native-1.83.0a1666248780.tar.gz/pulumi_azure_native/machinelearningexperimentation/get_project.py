# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    """
    An object that represents a machine learning project.
    """
    def __init__(__self__, account_id=None, creation_date=None, description=None, friendly_name=None, gitrepo=None, id=None, location=None, name=None, project_id=None, provisioning_state=None, tags=None, type=None, workspace_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if gitrepo and not isinstance(gitrepo, str):
            raise TypeError("Expected argument 'gitrepo' to be a str")
        pulumi.set(__self__, "gitrepo", gitrepo)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The immutable id of the team account which contains this project.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of the project in ISO8601 format.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of this project.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> str:
        """
        The friendly name for this project.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def gitrepo(self) -> Optional[str]:
        """
        The reference to git repo for this project.
        """
        return pulumi.get(self, "gitrepo")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The immutable id of this project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of project resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> str:
        """
        The immutable id of the workspace which contains this project.
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            account_id=self.account_id,
            creation_date=self.creation_date,
            description=self.description,
            friendly_name=self.friendly_name,
            gitrepo=self.gitrepo,
            id=self.id,
            location=self.location,
            name=self.name,
            project_id=self.project_id,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            workspace_id=self.workspace_id)


def get_project(account_name: Optional[str] = None,
                project_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                workspace_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    An object that represents a machine learning project.
    API Version: 2017-05-01-preview.


    :param str account_name: The name of the machine learning team account.
    :param str project_name: The name of the machine learning project under a team account workspace.
    :param str resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :param str workspace_name: The name of the machine learning team account workspace.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningexperimentation:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        account_id=__ret__.account_id,
        creation_date=__ret__.creation_date,
        description=__ret__.description,
        friendly_name=__ret__.friendly_name,
        gitrepo=__ret__.gitrepo,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        project_id=__ret__.project_id,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type,
        workspace_id=__ret__.workspace_id)


@_utilities.lift_output_func(get_project)
def get_project_output(account_name: Optional[pulumi.Input[str]] = None,
                       project_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       workspace_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    An object that represents a machine learning project.
    API Version: 2017-05-01-preview.


    :param str account_name: The name of the machine learning team account.
    :param str project_name: The name of the machine learning project under a team account workspace.
    :param str resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :param str workspace_name: The name of the machine learning team account workspace.
    """
    ...

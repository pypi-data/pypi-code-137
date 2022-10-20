# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['SourceControlArgs', 'SourceControl']

@pulumi.input_type
class SourceControlArgs:
    def __init__(__self__, *,
                 content_types: pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]],
                 display_name: pulumi.Input[str],
                 operational_insights_resource_provider: pulumi.Input[str],
                 repo_type: pulumi.Input[Union[str, 'RepoType']],
                 repository: pulumi.Input['RepositoryArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 source_control_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SourceControl resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]] content_types: Array of source control content types.
        :param pulumi.Input[str] display_name: The display name of the source control
        :param pulumi.Input[str] operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        :param pulumi.Input[Union[str, 'RepoType']] repo_type: The repository type of the source control
        :param pulumi.Input['RepositoryArgs'] repository: Repository metadata.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[str] description: A description of the source control
        :param pulumi.Input[str] id: The id (a Guid) of the source control
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] source_control_id: Source control Id
        """
        pulumi.set(__self__, "content_types", content_types)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "operational_insights_resource_provider", operational_insights_resource_provider)
        pulumi.set(__self__, "repo_type", repo_type)
        pulumi.set(__self__, "repository", repository)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if source_control_id is not None:
            pulumi.set(__self__, "source_control_id", source_control_id)

    @property
    @pulumi.getter(name="contentTypes")
    def content_types(self) -> pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]]:
        """
        Array of source control content types.
        """
        return pulumi.get(self, "content_types")

    @content_types.setter
    def content_types(self, value: pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]]):
        pulumi.set(self, "content_types", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the source control
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="operationalInsightsResourceProvider")
    def operational_insights_resource_provider(self) -> pulumi.Input[str]:
        """
        The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        """
        return pulumi.get(self, "operational_insights_resource_provider")

    @operational_insights_resource_provider.setter
    def operational_insights_resource_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "operational_insights_resource_provider", value)

    @property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Input[Union[str, 'RepoType']]:
        """
        The repository type of the source control
        """
        return pulumi.get(self, "repo_type")

    @repo_type.setter
    def repo_type(self, value: pulumi.Input[Union[str, 'RepoType']]):
        pulumi.set(self, "repo_type", value)

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Input['RepositoryArgs']:
        """
        Repository metadata.
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: pulumi.Input['RepositoryArgs']):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @created_by_type.setter
    def created_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "created_by_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the source control
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The id (a Guid) of the source control
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_at", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @last_modified_by_type.setter
    def last_modified_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "last_modified_by_type", value)

    @property
    @pulumi.getter(name="sourceControlId")
    def source_control_id(self) -> Optional[pulumi.Input[str]]:
        """
        Source control Id
        """
        return pulumi.get(self, "source_control_id")

    @source_control_id.setter
    def source_control_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_control_id", value)


class SourceControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                 repo_type: Optional[pulumi.Input[Union[str, 'RepoType']]] = None,
                 repository: Optional[pulumi.Input[pulumi.InputType['RepositoryArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_control_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a SourceControl in Azure Security Insights.
        API Version: 2021-03-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]] content_types: Array of source control content types.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[str] description: A description of the source control
        :param pulumi.Input[str] display_name: The display name of the source control
        :param pulumi.Input[str] id: The id (a Guid) of the source control
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        :param pulumi.Input[Union[str, 'RepoType']] repo_type: The repository type of the source control
        :param pulumi.Input[pulumi.InputType['RepositoryArgs']] repository: Repository metadata.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source_control_id: Source control Id
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SourceControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a SourceControl in Azure Security Insights.
        API Version: 2021-03-01-preview.

        :param str resource_name: The name of the resource.
        :param SourceControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SourceControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ContentType']]]]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                 repo_type: Optional[pulumi.Input[Union[str, 'RepoType']]] = None,
                 repository: Optional[pulumi.Input[pulumi.InputType['RepositoryArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_control_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SourceControlArgs.__new__(SourceControlArgs)

            if content_types is None and not opts.urn:
                raise TypeError("Missing required property 'content_types'")
            __props__.__dict__["content_types"] = content_types
            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["created_by_type"] = created_by_type
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["id"] = id
            __props__.__dict__["last_modified_at"] = last_modified_at
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["last_modified_by_type"] = last_modified_by_type
            if operational_insights_resource_provider is None and not opts.urn:
                raise TypeError("Missing required property 'operational_insights_resource_provider'")
            __props__.__dict__["operational_insights_resource_provider"] = operational_insights_resource_provider
            if repo_type is None and not opts.urn:
                raise TypeError("Missing required property 'repo_type'")
            __props__.__dict__["repo_type"] = repo_type
            if repository is None and not opts.urn:
                raise TypeError("Missing required property 'repository'")
            __props__.__dict__["repository"] = repository
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source_control_id"] = source_control_id
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:SourceControl"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:SourceControl")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SourceControl, __self__).__init__(
            'azure-native:securityinsights:SourceControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SourceControl':
        """
        Get an existing SourceControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SourceControlArgs.__new__(SourceControlArgs)

        __props__.__dict__["content_types"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_by_type"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_by_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["repo_type"] = None
        __props__.__dict__["repository"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SourceControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentTypes")
    def content_types(self) -> pulumi.Output[Sequence[str]]:
        """
        Array of source control content types.
        """
        return pulumi.get(self, "content_types")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the source control
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the source control
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Output[str]:
        """
        The repository type of the source control
        """
        return pulumi.get(self, "repo_type")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output['outputs.RepositoryResponse']:
        """
        Repository metadata.
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


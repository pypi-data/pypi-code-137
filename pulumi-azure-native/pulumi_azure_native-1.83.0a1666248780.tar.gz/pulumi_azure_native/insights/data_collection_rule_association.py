# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DataCollectionRuleAssociationArgs', 'DataCollectionRuleAssociation']

@pulumi.input_type
class DataCollectionRuleAssociationArgs:
    def __init__(__self__, *,
                 resource_uri: pulumi.Input[str],
                 association_name: Optional[pulumi.Input[str]] = None,
                 data_collection_rule_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataCollectionRuleAssociation resource.
        :param pulumi.Input[str] resource_uri: The identifier of the resource.
        :param pulumi.Input[str] association_name: The name of the association. The name is case insensitive.
        :param pulumi.Input[str] data_collection_rule_id: The resource ID of the data collection rule that is to be associated.
        :param pulumi.Input[str] description: Description of the association.
        """
        pulumi.set(__self__, "resource_uri", resource_uri)
        if association_name is not None:
            pulumi.set(__self__, "association_name", association_name)
        if data_collection_rule_id is not None:
            pulumi.set(__self__, "data_collection_rule_id", data_collection_rule_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[str]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter(name="associationName")
    def association_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the association. The name is case insensitive.
        """
        return pulumi.get(self, "association_name")

    @association_name.setter
    def association_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "association_name", value)

    @property
    @pulumi.getter(name="dataCollectionRuleId")
    def data_collection_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the data collection rule that is to be associated.
        """
        return pulumi.get(self, "data_collection_rule_id")

    @data_collection_rule_id.setter
    def data_collection_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_collection_rule_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the association.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class DataCollectionRuleAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 association_name: Optional[pulumi.Input[str]] = None,
                 data_collection_rule_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of generic ARM proxy resource.
        API Version: 2019-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_name: The name of the association. The name is case insensitive.
        :param pulumi.Input[str] data_collection_rule_id: The resource ID of the data collection rule that is to be associated.
        :param pulumi.Input[str] description: Description of the association.
        :param pulumi.Input[str] resource_uri: The identifier of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataCollectionRuleAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of generic ARM proxy resource.
        API Version: 2019-11-01-preview.

        :param str resource_name: The name of the resource.
        :param DataCollectionRuleAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataCollectionRuleAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 association_name: Optional[pulumi.Input[str]] = None,
                 data_collection_rule_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataCollectionRuleAssociationArgs.__new__(DataCollectionRuleAssociationArgs)

            __props__.__dict__["association_name"] = association_name
            __props__.__dict__["data_collection_rule_id"] = data_collection_rule_id
            __props__.__dict__["description"] = description
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20191101preview:DataCollectionRuleAssociation"), pulumi.Alias(type_="azure-native:insights/v20210401:DataCollectionRuleAssociation"), pulumi.Alias(type_="azure-native:insights/v20210901preview:DataCollectionRuleAssociation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataCollectionRuleAssociation, __self__).__init__(
            'azure-native:insights:DataCollectionRuleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataCollectionRuleAssociation':
        """
        Get an existing DataCollectionRuleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataCollectionRuleAssociationArgs.__new__(DataCollectionRuleAssociationArgs)

        __props__.__dict__["data_collection_rule_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return DataCollectionRuleAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataCollectionRuleId")
    def data_collection_rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the data collection rule that is to be associated.
        """
        return pulumi.get(self, "data_collection_rule_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the association.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource entity tag (ETag).
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


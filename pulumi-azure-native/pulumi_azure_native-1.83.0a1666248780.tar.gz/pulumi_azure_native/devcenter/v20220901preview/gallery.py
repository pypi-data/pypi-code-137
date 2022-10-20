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

__all__ = ['GalleryArgs', 'Gallery']

@pulumi.input_type
class GalleryArgs:
    def __init__(__self__, *,
                 dev_center_name: pulumi.Input[str],
                 gallery_resource_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 gallery_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Gallery resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[str] gallery_resource_id: The resource ID of the backing Azure Compute Gallery.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input[str] gallery_name: The name of the gallery.
        """
        pulumi.set(__self__, "dev_center_name", dev_center_name)
        pulumi.set(__self__, "gallery_resource_id", gallery_resource_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if gallery_name is not None:
            pulumi.set(__self__, "gallery_name", gallery_name)

    @property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[str]:
        """
        The name of the devcenter.
        """
        return pulumi.get(self, "dev_center_name")

    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dev_center_name", value)

    @property
    @pulumi.getter(name="galleryResourceId")
    def gallery_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the backing Azure Compute Gallery.
        """
        return pulumi.get(self, "gallery_resource_id")

    @gallery_resource_id.setter
    def gallery_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gallery_resource_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the gallery.
        """
        return pulumi.get(self, "gallery_name")

    @gallery_name.setter
    def gallery_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gallery_name", value)


class Gallery(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 gallery_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a gallery.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[str] gallery_name: The name of the gallery.
        :param pulumi.Input[str] gallery_resource_id: The resource ID of the backing Azure Compute Gallery.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GalleryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a gallery.

        :param str resource_name: The name of the resource.
        :param GalleryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GalleryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 gallery_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GalleryArgs.__new__(GalleryArgs)

            if dev_center_name is None and not opts.urn:
                raise TypeError("Missing required property 'dev_center_name'")
            __props__.__dict__["dev_center_name"] = dev_center_name
            __props__.__dict__["gallery_name"] = gallery_name
            if gallery_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'gallery_resource_id'")
            __props__.__dict__["gallery_resource_id"] = gallery_resource_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:Gallery"), pulumi.Alias(type_="azure-native:devcenter/v20220801preview:Gallery"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:Gallery")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Gallery, __self__).__init__(
            'azure-native:devcenter/v20220901preview:Gallery',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gallery':
        """
        Get an existing Gallery resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GalleryArgs.__new__(GalleryArgs)

        __props__.__dict__["gallery_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Gallery(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="galleryResourceId")
    def gallery_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the backing Azure Compute Gallery.
        """
        return pulumi.get(self, "gallery_resource_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


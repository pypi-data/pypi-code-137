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
    'GetProductResult',
    'AwaitableGetProductResult',
    'get_product',
    'get_product_output',
]

@pulumi.output_type
class GetProductResult:
    """
    Product details.
    """
    def __init__(__self__, approval_required=None, description=None, display_name=None, id=None, name=None, state=None, subscription_required=None, subscriptions_limit=None, terms=None, type=None):
        if approval_required and not isinstance(approval_required, bool):
            raise TypeError("Expected argument 'approval_required' to be a bool")
        pulumi.set(__self__, "approval_required", approval_required)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subscription_required and not isinstance(subscription_required, bool):
            raise TypeError("Expected argument 'subscription_required' to be a bool")
        pulumi.set(__self__, "subscription_required", subscription_required)
        if subscriptions_limit and not isinstance(subscriptions_limit, int):
            raise TypeError("Expected argument 'subscriptions_limit' to be a int")
        pulumi.set(__self__, "subscriptions_limit", subscriptions_limit)
        if terms and not isinstance(terms, str):
            raise TypeError("Expected argument 'terms' to be a str")
        pulumi.set(__self__, "terms", terms)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[bool]:
        """
        whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of true.
        """
        return pulumi.get(self, "approval_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Product description. May include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Product name.
        """
        return pulumi.get(self, "display_name")

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
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> Optional[bool]:
        """
        Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.
        """
        return pulumi.get(self, "subscription_required")

    @property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> Optional[int]:
        """
        Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of true.
        """
        return pulumi.get(self, "subscriptions_limit")

    @property
    @pulumi.getter
    def terms(self) -> Optional[str]:
        """
        Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
        """
        return pulumi.get(self, "terms")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetProductResult(GetProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductResult(
            approval_required=self.approval_required,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            state=self.state,
            subscription_required=self.subscription_required,
            subscriptions_limit=self.subscriptions_limit,
            terms=self.terms,
            type=self.type)


def get_product(product_id: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductResult:
    """
    Product details.


    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['productId'] = product_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20191201:getProduct', __args__, opts=opts, typ=GetProductResult).value

    return AwaitableGetProductResult(
        approval_required=__ret__.approval_required,
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        name=__ret__.name,
        state=__ret__.state,
        subscription_required=__ret__.subscription_required,
        subscriptions_limit=__ret__.subscriptions_limit,
        terms=__ret__.terms,
        type=__ret__.type)


@_utilities.lift_output_func(get_product)
def get_product_output(product_id: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProductResult]:
    """
    Product details.


    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...

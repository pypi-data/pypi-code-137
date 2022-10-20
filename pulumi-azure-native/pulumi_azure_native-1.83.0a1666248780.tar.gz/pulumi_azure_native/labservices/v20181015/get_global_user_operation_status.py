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
    'GetGlobalUserOperationStatusResult',
    'AwaitableGetGlobalUserOperationStatusResult',
    'get_global_user_operation_status',
    'get_global_user_operation_status_output',
]

@pulumi.output_type
class GetGlobalUserOperationStatusResult:
    """
    Status Details of the long running operation for an environment
    """
    def __init__(__self__, status=None):
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        status of the long running operation for an environment
        """
        return pulumi.get(self, "status")


class AwaitableGetGlobalUserOperationStatusResult(GetGlobalUserOperationStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGlobalUserOperationStatusResult(
            status=self.status)


def get_global_user_operation_status(operation_url: Optional[str] = None,
                                     user_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGlobalUserOperationStatusResult:
    """
    Status Details of the long running operation for an environment


    :param str operation_url: The operation url of long running operation
    :param str user_name: The name of the user.
    """
    __args__ = dict()
    __args__['operationUrl'] = operation_url
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20181015:getGlobalUserOperationStatus', __args__, opts=opts, typ=GetGlobalUserOperationStatusResult).value

    return AwaitableGetGlobalUserOperationStatusResult(
        status=__ret__.status)


@_utilities.lift_output_func(get_global_user_operation_status)
def get_global_user_operation_status_output(operation_url: Optional[pulumi.Input[str]] = None,
                                            user_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGlobalUserOperationStatusResult]:
    """
    Status Details of the long running operation for an environment


    :param str operation_url: The operation url of long running operation
    :param str user_name: The name of the user.
    """
    ...

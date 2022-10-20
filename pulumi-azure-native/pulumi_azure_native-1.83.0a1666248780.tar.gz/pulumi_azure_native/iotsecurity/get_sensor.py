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

__all__ = [
    'GetSensorResult',
    'AwaitableGetSensorResult',
    'get_sensor',
    'get_sensor_output',
]

@pulumi.output_type
class GetSensorResult:
    """
    IoT sensor model
    """
    def __init__(__self__, connectivity_time=None, dynamic_learning=None, id=None, learning_mode=None, name=None, sensor_status=None, sensor_type=None, sensor_version=None, system_data=None, ti_automatic_updates=None, ti_status=None, ti_version=None, type=None, zone=None):
        if connectivity_time and not isinstance(connectivity_time, str):
            raise TypeError("Expected argument 'connectivity_time' to be a str")
        pulumi.set(__self__, "connectivity_time", connectivity_time)
        if dynamic_learning and not isinstance(dynamic_learning, bool):
            raise TypeError("Expected argument 'dynamic_learning' to be a bool")
        pulumi.set(__self__, "dynamic_learning", dynamic_learning)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if learning_mode and not isinstance(learning_mode, bool):
            raise TypeError("Expected argument 'learning_mode' to be a bool")
        pulumi.set(__self__, "learning_mode", learning_mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sensor_status and not isinstance(sensor_status, str):
            raise TypeError("Expected argument 'sensor_status' to be a str")
        pulumi.set(__self__, "sensor_status", sensor_status)
        if sensor_type and not isinstance(sensor_type, str):
            raise TypeError("Expected argument 'sensor_type' to be a str")
        pulumi.set(__self__, "sensor_type", sensor_type)
        if sensor_version and not isinstance(sensor_version, str):
            raise TypeError("Expected argument 'sensor_version' to be a str")
        pulumi.set(__self__, "sensor_version", sensor_version)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if ti_automatic_updates and not isinstance(ti_automatic_updates, bool):
            raise TypeError("Expected argument 'ti_automatic_updates' to be a bool")
        pulumi.set(__self__, "ti_automatic_updates", ti_automatic_updates)
        if ti_status and not isinstance(ti_status, str):
            raise TypeError("Expected argument 'ti_status' to be a str")
        pulumi.set(__self__, "ti_status", ti_status)
        if ti_version and not isinstance(ti_version, str):
            raise TypeError("Expected argument 'ti_version' to be a str")
        pulumi.set(__self__, "ti_version", ti_version)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="connectivityTime")
    def connectivity_time(self) -> str:
        """
        Last connectivity time of the IoT sensor
        """
        return pulumi.get(self, "connectivity_time")

    @property
    @pulumi.getter(name="dynamicLearning")
    def dynamic_learning(self) -> bool:
        """
        Dynamic mode status of the IoT sensor
        """
        return pulumi.get(self, "dynamic_learning")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="learningMode")
    def learning_mode(self) -> bool:
        """
        Learning mode status of the IoT sensor
        """
        return pulumi.get(self, "learning_mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sensorStatus")
    def sensor_status(self) -> str:
        """
        Status of the IoT sensor
        """
        return pulumi.get(self, "sensor_status")

    @property
    @pulumi.getter(name="sensorType")
    def sensor_type(self) -> Optional[str]:
        """
        Type of sensor
        """
        return pulumi.get(self, "sensor_type")

    @property
    @pulumi.getter(name="sensorVersion")
    def sensor_version(self) -> str:
        """
        Version of the IoT sensor
        """
        return pulumi.get(self, "sensor_version")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tiAutomaticUpdates")
    def ti_automatic_updates(self) -> Optional[bool]:
        """
        TI Automatic mode status of the IoT sensor
        """
        return pulumi.get(self, "ti_automatic_updates")

    @property
    @pulumi.getter(name="tiStatus")
    def ti_status(self) -> str:
        """
        TI Status of the IoT sensor
        """
        return pulumi.get(self, "ti_status")

    @property
    @pulumi.getter(name="tiVersion")
    def ti_version(self) -> str:
        """
        TI Version of the IoT sensor
        """
        return pulumi.get(self, "ti_version")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        """
        Zone of the IoT sensor
        """
        return pulumi.get(self, "zone")


class AwaitableGetSensorResult(GetSensorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSensorResult(
            connectivity_time=self.connectivity_time,
            dynamic_learning=self.dynamic_learning,
            id=self.id,
            learning_mode=self.learning_mode,
            name=self.name,
            sensor_status=self.sensor_status,
            sensor_type=self.sensor_type,
            sensor_version=self.sensor_version,
            system_data=self.system_data,
            ti_automatic_updates=self.ti_automatic_updates,
            ti_status=self.ti_status,
            ti_version=self.ti_version,
            type=self.type,
            zone=self.zone)


def get_sensor(scope: Optional[str] = None,
               sensor_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSensorResult:
    """
    IoT sensor model
    API Version: 2021-02-01-preview.


    :param str scope: Scope of the query (IoT Hub, /providers/Microsoft.Devices/iotHubs/myHub)
    :param str sensor_name: Name of the IoT sensor
    """
    __args__ = dict()
    __args__['scope'] = scope
    __args__['sensorName'] = sensor_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotsecurity:getSensor', __args__, opts=opts, typ=GetSensorResult).value

    return AwaitableGetSensorResult(
        connectivity_time=__ret__.connectivity_time,
        dynamic_learning=__ret__.dynamic_learning,
        id=__ret__.id,
        learning_mode=__ret__.learning_mode,
        name=__ret__.name,
        sensor_status=__ret__.sensor_status,
        sensor_type=__ret__.sensor_type,
        sensor_version=__ret__.sensor_version,
        system_data=__ret__.system_data,
        ti_automatic_updates=__ret__.ti_automatic_updates,
        ti_status=__ret__.ti_status,
        ti_version=__ret__.ti_version,
        type=__ret__.type,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_sensor)
def get_sensor_output(scope: Optional[pulumi.Input[str]] = None,
                      sensor_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSensorResult]:
    """
    IoT sensor model
    API Version: 2021-02-01-preview.


    :param str scope: Scope of the query (IoT Hub, /providers/Microsoft.Devices/iotHubs/myHub)
    :param str sensor_name: Name of the IoT sensor
    """
    ...

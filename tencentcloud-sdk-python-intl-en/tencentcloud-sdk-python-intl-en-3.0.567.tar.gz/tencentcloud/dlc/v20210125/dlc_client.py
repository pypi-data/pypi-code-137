# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dlc.v20210125 import models


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.tencentcloudapi.com'
    _service = 'dlc'


    def CancelTask(self, request):
        """This API is used to cancel a task.

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSparkApp(self, request):
        """This API is used to create a Spark application.

        :param request: Request instance for CreateSparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkApp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSparkAppResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSparkAppTask(self, request):
        """This API is used to create a Spark task.

        :param request: Request instance for CreateSparkAppTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkAppTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSparkAppTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTask(self, request):
        """This API is used to create a SQL query task. (We recommend you use the `CreateTasks` API instead.)

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTasks(self, request):
        """This API is used to create tasks in batches.

        :param request: Request instance for CreateTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSparkApp(self, request):
        """This API is used to delete a Spark application.

        :param request: Request instance for DeleteSparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteSparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteSparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSparkApp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSparkAppResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkAppJob(self, request):
        """This API is used to query a specific Spark application.

        :param request: Request instance for DescribeSparkAppJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSparkAppJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkAppJobs(self, request):
        """This API is used to get the list of Spark applications.

        :param request: Request instance for DescribeSparkAppJobs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSparkAppJobsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkAppTasks(self, request):
        """This API is used to query the list of running task instances of a Spark application.

        :param request: Request instance for DescribeSparkAppTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSparkAppTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResult(self, request):
        """This API is used to query the result of a task.

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """This API is used to query the list of tasks.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySparkApp(self, request):
        """This API is used to update a Spark application.

        :param request: Request instance for ModifySparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySparkApp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySparkAppResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)
# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.22-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import killbill
from killbill.api.overdue_api import OverdueApi  # noqa: E501
from killbill.rest import ApiException


class TestOverdueApi(unittest.TestCase):
    """OverdueApi unit test stubs"""

    def setUp(self):
        self.api = killbill.api.overdue_api.OverdueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_overdue_config_json(self):
        """Test case for get_overdue_config_json

        Retrieve the overdue config as JSON  # noqa: E501
        """
        pass

    def test_get_overdue_config_xml(self):
        """Test case for get_overdue_config_xml

        Retrieve the overdue config as XML  # noqa: E501
        """
        pass

    def test_upload_overdue_config_json(self):
        """Test case for upload_overdue_config_json

        Upload the full overdue config as JSON  # noqa: E501
        """
        pass

    def test_upload_overdue_config_xml(self):
        """Test case for upload_overdue_config_xml

        Upload the full overdue config as XML  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

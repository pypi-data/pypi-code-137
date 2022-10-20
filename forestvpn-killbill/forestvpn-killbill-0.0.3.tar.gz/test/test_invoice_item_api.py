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
from killbill.api.invoice_item_api import InvoiceItemApi  # noqa: E501
from killbill.rest import ApiException


class TestInvoiceItemApi(unittest.TestCase):
    """InvoiceItemApi unit test stubs"""

    def setUp(self):
        self.api = killbill.api.invoice_item_api.InvoiceItemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_invoice_item_custom_fields(self):
        """Test case for create_invoice_item_custom_fields

        Add custom fields to invoice item  # noqa: E501
        """
        pass

    def test_create_invoice_item_tags(self):
        """Test case for create_invoice_item_tags

        Add tags to invoice item  # noqa: E501
        """
        pass

    def test_delete_invoice_item_custom_fields(self):
        """Test case for delete_invoice_item_custom_fields

        Remove custom fields from invoice item  # noqa: E501
        """
        pass

    def test_delete_invoice_item_tags(self):
        """Test case for delete_invoice_item_tags

        Remove tags from invoice item  # noqa: E501
        """
        pass

    def test_get_invoice_item_audit_logs_with_history(self):
        """Test case for get_invoice_item_audit_logs_with_history

        Retrieve invoice item audit logs with history by id  # noqa: E501
        """
        pass

    def test_get_invoice_item_custom_fields(self):
        """Test case for get_invoice_item_custom_fields

        Retrieve invoice item custom fields  # noqa: E501
        """
        pass

    def test_get_invoice_item_tags(self):
        """Test case for get_invoice_item_tags

        Retrieve invoice item tags  # noqa: E501
        """
        pass

    def test_modify_invoice_item_custom_fields(self):
        """Test case for modify_invoice_item_custom_fields

        Modify custom fields to invoice item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

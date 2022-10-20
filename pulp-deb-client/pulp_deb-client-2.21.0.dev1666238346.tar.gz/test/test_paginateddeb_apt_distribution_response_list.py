# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_deb
from pulpcore.client.pulp_deb.models.paginateddeb_apt_distribution_response_list import PaginateddebAptDistributionResponseList  # noqa: E501
from pulpcore.client.pulp_deb.rest import ApiException

class TestPaginateddebAptDistributionResponseList(unittest.TestCase):
    """PaginateddebAptDistributionResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginateddebAptDistributionResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_deb.models.paginateddeb_apt_distribution_response_list.PaginateddebAptDistributionResponseList()  # noqa: E501
        if include_optional :
            return PaginateddebAptDistributionResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_deb.models.deb/apt_distribution_response.deb.AptDistributionResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        base_path = '0', 
                        base_url = '0', 
                        content_guard = '0', 
                        pulp_labels = pulpcore.client.pulp_deb.models.pulp_labels.pulp_labels(), 
                        name = '0', 
                        repository = '0', 
                        publication = '0', )
                    ]
            )
        else :
            return PaginateddebAptDistributionResponseList(
        )

    def testPaginateddebAptDistributionResponseList(self):
        """Test PaginateddebAptDistributionResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

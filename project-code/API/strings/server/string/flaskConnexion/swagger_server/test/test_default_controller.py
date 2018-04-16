# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_string_str_get(self):
        """Test case for add_string_str_get

        
        """
        response = self.client.open(
            '/cloudmesh/strings//addString/{str}'.format(str='str_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_string_id_get(self):
        """Test case for fetch_string_id_get

        
        """
        response = self.client.open(
            '/cloudmesh/strings//fetchString/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

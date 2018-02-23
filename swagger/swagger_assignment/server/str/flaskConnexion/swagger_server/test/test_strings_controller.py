# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestStringsController(BaseTestCase):
    """StringsController integration test stubs"""

    def test_add_str(self):
        """Test case for add_str

        Add the string
        """
        query_string = [('str', 'str_example')]
        response = self.client.open(
            '/v2/addString',
            method='GET',
            content_type='string',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_str(self):
        """Test case for fetch_str

        Get the string by id
        """
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/v2/fetchString',
            method='GET',
            content_type='string',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_match_str(self):
        """Test case for match_str

        String Match
        """
        query_string = [('subStr', 'subStr_example'),
                        ('str', 'str_example')]
        response = self.client.open(
            '/v2/getMatchData',
            method='GET',
            content_type='string',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parse_str(self):
        """Test case for parse_str

        List 1. all the unique characters; 2. numeric digits count
        """
        query_string = [('str', 'str_example')]
        response = self.client.open(
            '/v2/parseString',
            method='GET',
            content_type='string',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_str(self):
        """Test case for replace_str

        Replace one old str with the new one
        """
        query_string = [('oldStr', 'oldStr_example'),
                        ('newStr', 'newStr_example'),
                        ('str', 'str_example')]
        response = self.client.open(
            '/v2/replaceString',
            method='GET',
            content_type='string',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

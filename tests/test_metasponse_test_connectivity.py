# File: test_metasponse_test_connectivity.py
#
# Copyright (c) 2023-2025 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import json
import unittest
from unittest.mock import patch

import metasponse_consts as consts
from metasponse_connector import MetasponseConnector
from tests import metasponse_config


@patch("metasponse_utils.requests.get")
class TestConnectivityAction(unittest.TestCase):
    """Class to test the Test Connectivity action."""

    def setUp(self):
        self.connector = MetasponseConnector()
        self.test_json = dict(metasponse_config.TEST_JSON)
        self.test_json.update({"action": "test connectivity", "identifier": "test_connectivity"})

        return super().setUp()

    def test_connectivity_pass(self, mock_get):
        """
        Test the valid case for the test connectivity action.

        Patch the get() to return all plugins.
        """

        mock_get.return_value.status_code = 200
        mock_get.return_value.headers = metasponse_config.DEFAULT_HEADERS
        mock_get.return_value.json.return_value = {"id": "plugin_id", "name": "plugin_name", "path": "plugin_path", "type": "plugin_type"}

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)

        self.assertEqual(ret_val["result_summary"]["total_objects"], 1)
        self.assertEqual(ret_val["result_summary"]["total_objects_successful"], 1)
        self.assertEqual(ret_val["status"], "success")

        mock_get.assert_called_with(
            f"{self.test_json['config']['base_url']}{consts.METASPONSE_LIST_PLUGINS}",
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={},
        )

    def test_connectivity_invalid_base_url_fail(self, mock_get):
        """
        Test the invalid case for the test connectivity action.

        Patch the get() to return all plugins.
        """
        mock_get.side_effect = Exception("Connection timeout")
        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val["result_summary"]["total_objects"], 1)
        self.assertEqual(ret_val["result_summary"]["total_objects_successful"], 0)
        self.assertEqual(ret_val["status"], "failed")

        mock_get.assert_called_with(
            f"{self.test_json['config']['base_url']}{consts.METASPONSE_LIST_PLUGINS}",
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={},
        )

# File: test_metasponse_kill_job.py
#
# Copyright (c) 2023 Splunk Inc.
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
from tests import config


@patch("metasponse_utils.requests.delete")
class GetJobStatusAction(unittest.TestCase):
    """Class to test the kill job status action."""

    def setUp(self):

        self.connector = MetasponseConnector()
        self.test_json = dict(config.TEST_JSON)
        self.test_json.update({"action": "kill job", "identifier": "kill_job"})

        return super().setUp()

    def test_kill_job_status_valid(self, mock_delete):
        """
        Test the valid case for the get job status action.

        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job"
        }]

        mock_delete.return_value.status_code = 200
        mock_delete.return_value.headers = config.DEFAULT_HEADERS
        mock_delete.return_value.json.return_value = {}

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)

        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 1)
        self.assertEqual(ret_val['status'], 'success')

        endpoint = consts.METASPONSE_KILL_JOB.format(job_name="test_job")
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )

    def test_kill_job_status_invalid(self, mock_delete):
        """
        Test the invalid case for the get job status action.

        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job"
        }]

        mock_delete.return_value.status_code = 404
        mock_delete.return_value.headers = config.DEFAULT_HEADERS
        mock_delete.return_value.json.return_value = [{"error": "job not found"}]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        endpoint = consts.METASPONSE_KILL_JOB.format(job_name="test_job")
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )

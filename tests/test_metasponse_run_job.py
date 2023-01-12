# File: test_metasponse_run_job.py
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


@patch("metasponse_utils.requests.post")
class RunJobAction(unittest.TestCase):
    """Class to test the Run Job action."""

    def setUp(self):

        self.connector = MetasponseConnector()
        self.test_json = dict(config.TEST_JSON)
        self.test_json.update({"action": "run job", "identifier": "run_job"})
        self.run_job_endpoint = consts.METASPONSE_RUN_JOB.format(builder_id="xxx-xxxx-xx-xxx-xx")

        return super().setUp()

    def test_run_job_valid(self, mock_post):
        """
        Test the valid case for the run job action.

        Patch the post() to run job.
        """

        self.test_json["parameters"] = [{
            "builder_id": "xxx-xxxx-xx-xxx-xx",
            "template": False
        }]

        mock_post.return_value.status_code = 200
        mock_post.return_value.headers = config.DEFAULT_HEADERS
        mock_post.return_value.json.return_value = {}

        req_data = {
            "template": False
        }

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 1)
        self.assertEqual(ret_val['status'], 'success')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.run_job_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data=req_data,
            headers={},
        )

    def test_run_job_with_delta_valid(self, mock_post):
        """
        Test the valid case for the run job action.

        Patch the post() to run job.
        """

        self.test_json["parameters"] = [{
            "builder_id": "xxx-xxxx-xx-xxx-xx",
            "template": False,
            "delta": 100
        }]

        mock_post.return_value.status_code = 200
        mock_post.return_value.headers = config.DEFAULT_HEADERS
        mock_post.return_value.json.return_value = {}

        req_data = {
            "template": False,
            "delta": 100
        }

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)

        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 1)
        self.assertEqual(ret_val['status'], 'success')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.run_job_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data=req_data,
            headers={},
        )

    def test_run_job_template_true_valid(self, mock_post):
        """
        Test the valid case for the run job action.

        Patch the post() to run job.
        """

        self.test_json["parameters"] = [{
            "builder_id": "xxx-xxxx-xx-xxx-xx",
            "template": True
        }]

        mock_post.return_value.status_code = 200
        mock_post.return_value.headers = config.DEFAULT_HEADERS
        mock_post.return_value.json.return_value = {}

        req_data = {
            "template": True
        }

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 1)
        self.assertEqual(ret_val['status'], 'success')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.run_job_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data=req_data,
            headers={},
        )

    def test_run_job_no_builderid_invalid(self, mock_post):
        """
        Test the invalid case for the run job action.

        Patch the post() to run job.
        """

        self.test_json["parameters"] = [{
            "builder_id": "xxx-xxxx-xx-xxx-xx",
            "template": False
        }]

        req_data = {
            "template": False
        }

        mock_post.return_value.status_code = 404
        mock_post.return_value.headers = config.DEFAULT_HEADERS
        mock_post.return_value.json.return_value = {"error": "builder not found"}

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.run_job_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data=req_data,
            headers={},
        )

    def test_run_job_negative_delta_invalid(self, mock_post):
        """
        Test the invalid case for the run job action.

        Patch the post() to run job.
        """

        self.test_json["parameters"] = [{
            "builder_id": "xxx-xxxx-xx-xxx-xx",
            "template": False,
            "delta": -10
        }]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

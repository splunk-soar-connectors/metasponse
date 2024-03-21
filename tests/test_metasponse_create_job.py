# File: test_metasponse_create_job.py
#
# Copyright (c) 2023-2024 Splunk Inc.
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

from requests import Response

import metasponse_consts as consts
from metasponse_connector import MetasponseConnector
from tests import metasponse_config


@patch("metasponse_utils.requests.delete")
@patch("metasponse_utils.requests.post")
@patch("metasponse_utils.requests.get")
class CreateJobAction(unittest.TestCase):
    """Class to test the Creat Job action."""

    def setUp(self):

        self.connector = MetasponseConnector()
        self.test_json = dict(metasponse_config.TEST_JSON)
        self.test_json.update({"action": "create job", "identifier": "create_job"})

        self.builder_endpoint = consts.METASPONSE_BUILDER_ENDPOINT.format(builder_id="xxx-xx-xxx-xxx")
        self.add_option_endpoint = f'{self.builder_endpoint}{consts.METASPONSE_ADD_OPTIONS.format(option_id="op_1")}'
        self.get_job_status_endpoint = f'{self.builder_endpoint}{consts.METASPONSE_CHECK_JOB_STATUS}'
        self.add_metadata_endpoint = f'{self.builder_endpoint}{consts.METASPONSE_ADD_JOB_METADATA}'
        self.delete_builder_endpoint = f'{self.builder_endpoint}{".json"}'
        self.add_plugins_endpoint = f'{self.builder_endpoint}{consts.METASPONSE_ADD_PLUGIN}'

        self.create_job_response_valid = Response()
        self.create_job_response_valid.status_code = 200
        self.create_job_response_valid.headers = metasponse_config.DEFAULT_HEADERS
        self.create_job_response_valid._content = b'{"builder_id": "xxx-xx-xxx-xxx", "error": null}'

        self.name_job_response_valid = Response()
        self.name_job_response_valid.status_code = 200
        self.name_job_response_valid.headers = metasponse_config.DEFAULT_HEADERS
        self.name_job_response_valid._content = b'{}'

        self.add_plugins_response_valid = Response()
        self.add_plugins_response_valid.status_code = 200
        self.add_plugins_response_valid.headers = metasponse_config.DEFAULT_HEADERS
        self.add_plugins_response_valid._content = b'{"new_options": [{"dummy_options":"dummy_values"}], ' \
                                                   b'"update_values": "dummy_values", "optional_errors": []}'

        self.add_options_response_valid = Response()
        self.add_options_response_valid.status_code = 200
        self.add_options_response_valid.headers = metasponse_config.DEFAULT_HEADERS
        self.add_options_response_valid._content = b'{"data": "dummy_data", "validation_errors":[]}'

        self.delete_builder_response = Response()
        self.delete_builder_response.headers = metasponse_config.DEFAULT_HEADERS
        self.delete_builder_response._content = b'{}'
        self.delete_builder_response.status_code = 200

        return super().setUp()

    def test_create_job_valid(self, mock_get, mock_post, mock_delete):
        """
        Test the valid case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        get_job_status_response = Response()
        get_job_status_response.status_code = 200
        get_job_status_response.headers = metasponse_config.DEFAULT_HEADERS
        get_job_status_response._content = b'{"data": "job_dummy_data", "is_ready": true, "plugin_order":["plugin1"]}'

        mock_post.side_effect = [self.create_job_response_valid, self.name_job_response_valid,
                                 self.add_plugins_response_valid, self.add_options_response_valid]
        mock_get.side_effect = [get_job_status_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 1)
        self.assertEqual(ret_val['status'], 'success')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_option_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"value": "val_1"},
            headers={}
        )

        mock_get.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.get_job_status_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 4)
        self.assertEqual(mock_get.call_count, 1)

    def test_create_job_no_builderid_invalid(self, mock_get, mock_post, mock_delete):
        """
        Test the no builder found case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        create_job_response = Response()
        create_job_response.status_code = 200
        create_job_response.headers = metasponse_config.DEFAULT_HEADERS
        create_job_response._content = b'{"error": "builder not found"}'

        mock_post.side_effect = [create_job_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)

        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{consts.METASPONSE_CREATE_JOB}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 1)

    def test_create_job_invalid_job_name(self, mock_get, mock_post, mock_delete):
        """
        Test job_name unique case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        name_job_response = Response()
        name_job_response.status_code = 400
        name_job_response.headers = metasponse_config.DEFAULT_HEADERS
        name_job_response._content = b'{"is_name_unique": false, "error": "Job name is not unique.Choose a unique name."}'

        mock_post.side_effect = [self.create_job_response_valid, name_job_response]
        mock_delete.side_effect = [self.delete_builder_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_metadata_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"name": "test_job"},
            headers={}
        )
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.delete_builder_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 2)
        self.assertEqual(mock_delete.call_count, 1)

    def test_create_job_invalid_plugins(self, mock_get, mock_post, mock_delete):
        """
        Test the invalid plugin case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        add_plugins_response = Response()
        add_plugins_response.status_code = 404
        add_plugins_response.headers = metasponse_config.DEFAULT_HEADERS
        add_plugins_response._content = b'{"error": "plugin not found"}'

        mock_post.side_effect = [self.create_job_response_valid, self.name_job_response_valid, add_plugins_response]
        mock_delete.side_effect = [self.delete_builder_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_plugins_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"plugin_id": "plugin1"},
            headers={}
        )
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.delete_builder_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 3)
        self.assertEqual(mock_delete.call_count, 1)

    def test_create_job_invalid_option(self, mock_get, mock_post, mock_delete):
        """
        Test the valid case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        add_options_response = Response()
        add_options_response.status_code = 404
        add_options_response.headers = metasponse_config.DEFAULT_HEADERS
        add_options_response._content = b'{"error": "option not found"}'

        mock_post.side_effect = [self.create_job_response_valid, self.name_job_response_valid,
                                 self.add_plugins_response_valid, add_options_response]
        mock_delete.side_effect = [self.delete_builder_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_option_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"value": "val_1"},
            headers={}
        )
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.delete_builder_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 4)
        self.assertEqual(mock_delete.call_count, 1)

    def test_create_job_invalid_option_value_1(self, mock_get, mock_post, mock_delete):
        """
        Test the invalid option value format case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """
        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "invalid format"
        }]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

    def test_create_job_invalid_option_value_2(self, mock_get, mock_post, mock_delete):
        """
        Test the invalid option value case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """
        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"\"}"
        }]

        add_options_response = Response()
        add_options_response.status_code = 200
        add_options_response.headers = metasponse_config.DEFAULT_HEADERS
        add_options_response._content = b'{"data": "dummy_data", "validation_errors":["missing required option value"]}'

        mock_post.side_effect = [self.create_job_response_valid, self.name_job_response_valid,
                                 self.add_plugins_response_valid, add_options_response]
        mock_delete.side_effect = [self.delete_builder_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_option_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"value": ""},
            headers={}
        )
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.delete_builder_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 4)
        self.assertEqual(mock_delete.call_count, 1)

    def test_create_job_invalid_job_status_1(self, mock_get, mock_post, mock_delete):
        """
        Test the false job status case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """
        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        get_job_status_response = Response()
        get_job_status_response.status_code = 200
        get_job_status_response.headers = metasponse_config.DEFAULT_HEADERS
        get_job_status_response._content = b'{"data": "job_dummy_data", "is_ready": false, "plugin_order":["plugin1"], ' \
                                           b'"error_msg": "Job check job failed check!:List of Errors: op_2: ' \
                                           b'value is required when op_1 is specified"}'

        mock_post.side_effect = [self.create_job_response_valid, self.name_job_response_valid,
                                 self.add_plugins_response_valid, self.add_options_response_valid]
        mock_get.side_effect = [get_job_status_response]
        mock_delete.side_effect = [self.delete_builder_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_option_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"value": "val_1"},
            headers={}
        )
        mock_get.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.get_job_status_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={},
        )
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.delete_builder_endpoint}',
            headers={},
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False
        )
        self.assertEqual(mock_post.call_count, 4)
        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_delete.call_count, 1)

    def test_create_job_invalid_job_status_2(self, mock_get, mock_post, mock_delete):
        """
        Test the invalid builder value provided for fetch the status case for the create job action.

        Patch the post() to create job, naming a job, add plugins and options.
        Patch the get() to return job status.
        """

        self.test_json["parameters"] = [{
            "job_name": "test_job",
            "job_plugins": "plugin1",
            "job_options": "{\"op_1\":\"val_1\"}"
        }]

        get_job_status_response = Response()
        get_job_status_response.status_code = 404
        get_job_status_response.headers = metasponse_config.DEFAULT_HEADERS
        get_job_status_response._content = b'{"error": "builder not found"}'

        mock_post.side_effect = [self.create_job_response_valid, self.name_job_response_valid,
                                 self.add_plugins_response_valid, self.add_options_response_valid]
        mock_get.side_effect = [get_job_status_response]
        mock_delete.side_effect = [self.delete_builder_response]

        ret_val = self.connector._handle_action(json.dumps(self.test_json), None)
        ret_val = json.loads(ret_val)
        self.assertEqual(ret_val['result_summary']['total_objects'], 1)
        self.assertEqual(ret_val['result_summary']['total_objects_successful'], 0)
        self.assertEqual(ret_val['status'], 'failed')

        mock_post.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.add_option_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            data={"value": "val_1"},
            headers={}
        )
        mock_get.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.get_job_status_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        mock_delete.assert_called_with(
            f'{self.test_json["config"]["base_url"]}{self.delete_builder_endpoint}',
            timeout=consts.METASPONSE_REQUEST_DEFAULT_TIMEOUT,
            verify=False,
            headers={}
        )
        self.assertEqual(mock_post.call_count, 4)
        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_delete.call_count, 1)

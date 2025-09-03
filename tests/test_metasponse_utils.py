# File: test_metasponse_utils.py
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

import unittest
from unittest.mock import Mock, patch

import requests
from phantom.action_result import ActionResult

from metasponse_utils import MetasponseUtils, RetVal


class TestRetValClass(unittest.TestCase):
    """Class to test the RetVal"""

    def test_ret_val_pass(self):
        """Tests the valid cases for the ret_val class."""
        test_cases = [
            ("single_value", [True], (True, None)),
            ("two_value", [True, {"key": "value"}], (True, {"key": "value"})),
        ]
        
        for case_name, input_val, expected in test_cases:
            with self.subTest(case=case_name):
                output = RetVal(*input_val)
                self.assertEqual(output, expected)


class TestValidateIntegerMethod(unittest.TestCase):
    """Class to test the validate_integer method."""

    def setUp(self):
        """Set up method for the tests."""
        self.util = MetasponseUtils(None)
        self.action_result = ActionResult({})
        return super().setUp()

    def test_validate_integer_pass(self):
        """Test the valid cases for the validate integer method."""
        test_cases = [
            ("zero_allowed", 0, 0, ""),
            ("integer", 10, 10.0, ""),
        ]
        
        for case_name, input_value, expected_value, expected_message in test_cases:
            with self.subTest(case=case_name):
                ret_val, output = self.util.validate_integer(self.action_result, input_value, "delta", True)
                self.assertTrue(ret_val)
                self.assertEqual(output, expected_value)
                self.assertEqual(self.action_result.get_message(), expected_message)

    def test_validate_integer_fail(self):
        """Test the failed cases for the validate integer method."""
        test_cases = [
            ("zero_not_allowed", "0", "Please provide a non-zero positive integer value in the 'delta' parameter"),
            ("alphanumeric", "abc12", "Please provide a valid integer value in the 'delta' parameter"),
            ("unicode", "ト日本標準時ﬗ╬⎋⅍ⅎ€", "Please provide a valid integer value in the 'delta' parameter"),
            ("float", "10.5", "Please provide a valid integer value in the 'delta' parameter"),
        ]
        
        for case_name, input_value, expected_message in test_cases:
            with self.subTest(case=case_name):
                ret_val, output = self.util.validate_integer(self.action_result, input_value, "delta", False)
                self.assertFalse(ret_val)
                self.assertIsNone(output)
                self.assertEqual(self.action_result.get_message(), expected_message)


class TestGetErrorMessageFromException(unittest.TestCase):
    """Class to test the get error message from exception method."""

    def setUp(self):
        """Set up method for the tests."""
        connector = Mock()
        connector.error_print.return_value = None
        self.util = MetasponseUtils(connector)
        self.action_result = ActionResult({})
        return super().setUp()

    def test_get_error_message_from_exception(self):
        """Test the pass and fail cases of get error message from exception method."""
        test_cases = [
            (
                "exception_without_args",
                Exception(),
                "Error message: Error message unavailable. Please check the asset configuration and|or action parameters",
            ),
            ("exception_with_single_arg", Exception("test message"), "Error message: test message"),
            ("exception_with_multiple_args", Exception("test code", "test message"), "Error code: test code. Error message: test message"),
        ]
        
        for case_name, input_value, expected_message in test_cases:
            with self.subTest(case=case_name):
                error_text = self.util._get_error_message_from_exception(input_value)
                self.assertEqual(error_text, expected_message)


class TestProcessEmptyResponse(unittest.TestCase):
    """Class to test the process empty response method."""

    def setUp(self):
        """Set up method for the tests."""
        self.response = Mock()
        self.util = MetasponseUtils(None)
        self.action_result = ActionResult({})
        return super().setUp()

    def test_process_empty_response(self):
        """Test the pass and fail cases of process empty response method."""
        test_cases = [
            ("success_code", 200, True, {}), 
            ("error_code", 404, False, None)
        ]
        
        for case_name, mock_code, expected_status, expected_value in test_cases:
            with self.subTest(case=case_name):
                self.response.status_code = mock_code
                status, value = self.util._process_empty_response(self.response, self.action_result)
                self.assertEqual(status, expected_status)
                self.assertEqual(value, expected_value)


class TestProcessHtmlResponse(unittest.TestCase):
    """Class to test the process html response method."""

    def setUp(self):
        """Set up method for the tests."""
        self.response = Mock()
        self.util = MetasponseUtils(None)
        self.action_result = ActionResult({})
        return super().setUp()

    def test_process_html_response(self):
        """Test the pass and fail cases of process html response method."""
        test_cases = [
            ("no_response_text", "", False, "Status code: 402, Data from server: Cannot parse error details"),
            ("normal_response", "Oops!<script>document.getElementById('demo')</script>", False, "Status code: 402, Data from server: Oops!"),
            ("large_response", "".join([str(i) for i in range(502)]), False, "Error parsing html response"),
        ]
        
        for case_name, response_value, expected_value, expected_message in test_cases:
            with self.subTest(case=case_name):
                if response_value:
                    self.response.text = response_value
                self.response.status_code = 402
                status, value = self.util._process_html_response(self.response, self.action_result)
                self.assertEqual(status, expected_value)
                self.assertEqual(self.action_result.get_message(), expected_message)
                self.assertIsNone(value)

    def test_process_response_html_fail(self):
        """Test the _process_response for html response."""
        response_obj = requests.Response()
        response_obj._content = b"<html><title>Login Page</title><body>Please login to the system.</body></html>"
        response_obj.status_code = 200
        response_obj.headers = {"Content-Type": "text/html; charset=utf-8"}

        ret_val, response = self.util._process_response(response_obj, self.action_result)
        self.assertFalse(ret_val)
        self.assertIsNone(response)


class TestProcessJsonResponse(unittest.TestCase):
    """Class to test the process json response method."""

    def setUp(self):
        """Set up method for the tests."""
        connector = Mock()
        connector.error_print.return_value = None
        self.response = Mock()
        self.util = MetasponseUtils(connector)
        self.action_result = ActionResult({})
        return super().setUp()

    def test_process_json_response(self):
        """Test the pass and fail cases of process json response method."""
        test_cases = [
            ("valid_success_json_response", 200, True, {"results": []}, {"results": []}),
            ("valid_failure_json_response", 404, False, {"status": "NOT_FOUND"}, None),
            ("invalid_json_response", 404, False, KeyError("Invalid Json"), None),
        ]
        
        for case_name, mock_code, expected_status, mock_response, expected_value in test_cases:
            with self.subTest(case=case_name):
                self.response.status_code = mock_code
                if "invalid_json_response" in case_name:
                    self.response.json.side_effect = mock_response
                else:
                    self.response.json.return_value = mock_response
                status, value = self.util._process_json_response(self.response, self.action_result)
                self.assertEqual(status, expected_status)
                self.assertEqual(value, expected_value)


class TestGeneralCases(unittest.TestCase):
    """Class to test the general cases."""

    def setUp(self):
        """Set up method for the tests."""
        connector = Mock()
        connector.error_print.return_value = None
        connector.config = {"base_url": "https://<base_url>/"}
        self.util = MetasponseUtils(connector)
        self.action_result = ActionResult({})
        return super().setUp()

    def test_make_rest_call_invalid_method(self):
        """Test the make_rest_call with invalid method."""
        ret_val, response = self.util.make_rest_call("/endpoint", self.action_result, method="invalid_method")
        self.assertFalse(ret_val)
        self.assertIsNone(response)
        self.assertEqual(self.action_result.get_message(), "Invalid method: invalid_method")

    @patch("metasponse_utils.requests.get")
    def test_make_rest_call_throw_exception(self, mock_get):
        """Test the make_rest_call for error case."""
        mock_get.side_effect = Exception("error code", "error message")

        ret_val, response = self.util.make_rest_call("/endpoint", self.action_result)
        self.assertFalse(ret_val)
        self.assertIsNone(response)
        self.assertEqual(self.action_result.get_message(), "Error Connecting to server. Details: ('error code', 'error message')")

    def test_process_response_unknown_fail(self):
        """Test the _process_response for unknown response."""
        response_obj = requests.Response()
        response_obj._content = b"dummy content"
        response_obj.status_code = 500
        response_obj.headers = {}

        ret_val, response = self.util._process_response(response_obj, self.action_result)
        self.assertFalse(ret_val)
        self.assertIsNone(response)
        self.assertIn("Can't process response from server. Status Code: 500 Data from server: dummy content", self.action_result.get_message())

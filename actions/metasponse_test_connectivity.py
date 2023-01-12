# File: metasponse_test_connectivity.py
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

import phantom.app as phantom

import metasponse_consts as consts
from actions import BaseAction


class TestConnectivityAction(BaseAction):
    """Class to handle test connectivity action."""

    def execute(self):
        self._connector.save_progress("Connecting to endpoint")
        self._connector.save_progress("Getting all jobs")

        ret_val, resposne = self._connector.util._make_rest_call(consts.METASPONSE_GET_ALL_JOBS, self._action_result, headers={})
        if phantom.is_fail(ret_val):
            self._connector.save_progress(consts.METASPONSE_ERROR_TEST_CONNECTIVITY)
            return self._action_result.get_status()

        self._connector.save_progress(consts.METASPONSE_SUCCESS_TEST_CONNECTIVITY)
        return self._action_result.set_status(phantom.APP_SUCCESS)

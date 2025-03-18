# File: metasponse_get_all_jobs.py
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

import phantom.app as phantom

import metasponse_consts as consts
from actions import BaseAction


class GetAllJobs(BaseAction):
    """Class to handle get all jobs status action."""

    def execute(self):
        """Execute get all jobs action."""

        ret_val, response = self._connector.util.make_rest_call(consts.METASPONSE_GET_ALL_JOBS, self._action_result, headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        [self._action_result.add_data(job) for job in response]
        self._action_result.update_summary({"total_jobs": len(response)})

        return self._action_result.set_status(phantom.APP_SUCCESS)

# File: metasponse_kill_job.py
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


class KillJob(BaseAction):
    """Class to handle kill job action."""

    def execute(self):
        job_name = self._param["job_name"]

        endpoint = consts.METASPONSE_KILL_JOB.format(job_name=job_name)

        ret_val, response = self._connector.util._make_rest_call(endpoint, self._action_result, method="delete", headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        return self._action_result.set_status(phantom.APP_SUCCESS, consts.METASPONSE_KILL_JOB_MESSAGE)

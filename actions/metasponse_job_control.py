# File: metasponse_job_control.py
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


class JobControl(BaseAction):
    """Class to handle job control action."""

    def execute(self):
        """Execute job control action."""

        job_name = self._param["job_name"]
        action = self._param.get("action")

        if action not in ["pickup", "abort"]:
            return self._action_result.set_status(phantom.APP_ERROR, consts.METASPONSE_ERROR_INVALID_ACTION_PARAM.format(key="action"))

        body = {
            "action": action
        }

        endpoint = consts.METASPONSE_PICK_UP_JOB_GET_JOB_STATUS.format(job_name=job_name)

        ret_val, response = self._connector.util._make_rest_call(endpoint, self._action_result, method="post", data=body, headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        return self._action_result.set_status(phantom.APP_SUCCESS, consts.METASPONSE_PICKUP_ABORT_JOB_MESSAGE.format(action=action))

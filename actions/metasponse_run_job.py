# File: metasponse_run_job.py
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


class RunJob(BaseAction):
    """Class to handle run job action."""

    def execute(self):
        """Execute run job action."""

        builder_id = self._param["builder_id"]
        delta = self._param.get("delta")
        template = self._param.get("template", False)
        body = {"template": template}

        if delta:
            ret_val, delta = self._connector.util.validate_integer(self._action_result, delta, "delta", allow_zero=True)
            if phantom.is_fail(ret_val):
                return self._action_result.get_status()
            body["delta"] = delta

        endpoint = consts.METASPONSE_RUN_JOB.format(builder_id=builder_id)
        ret_val, _ = self._connector.util.make_rest_call(endpoint, self._action_result, method="post", data=body, headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        if template:
            return self._action_result.set_status(phantom.APP_SUCCESS, consts.METASPONSE_JOB_TEMPLATE_MESSAGE)
        return self._action_result.set_status(phantom.APP_SUCCESS, consts.METASPONSE_JOB_SCHEDULED_MESSAGE)

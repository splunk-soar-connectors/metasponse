# File: metasponse_create_job.py
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

import phantom.app as phantom

import metasponse_consts as consts
from actions import BaseAction


class CreateJob(BaseAction):
    """Class to handle create job action."""

    def __init__(self, connector, param):
        """Prepare constructor define all job params.

        :param connector: Vision connector object
        :param param: Parameter dictionary
        """

        super().__init__(connector, param)
        self.job_name = None
        self.plugins = None
        self.job_options_dict = {}
        self.resp_json = {}
        self.builder_id = None
        self.builder_endpoint = None

    def initialize_params(self):
        self.job_name = self._param.get("job_name")
        self.plugins = [x.strip() for x in self._param.get("job_plugins").split(",")]
        self.plugins = list(set(filter(None, self.plugins)))
        if not self.plugins:
            return self._action_result.set_status(phantom.APP_ERROR, consts.METASPONSE_ERROR_INVALID_ACTION_PARAM.format(key="job_plugins"))

        ret_val, self.job_options_dict = self._connector.util.\
            validate_json_object(self._action_result, self._param["job_options"], "job_options")
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        return phantom.APP_SUCCESS

    def create_job(self):
        ret_val, response = self._connector.util.make_rest_call(consts.METASPONSE_CREATE_JOB, self._action_result, method="post",
                                                                 headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        if response.get("error"):
            self._action_result.add_data(response)
            return self._action_result.set_status(phantom.APP_ERROR, response.get("error"))

        self.builder_id = response.get("builder_id")
        self.builder_endpoint = consts.METASPONSE_BUILDER_ENDPOINT.format(builder_id=self.builder_id)

        # naming a job
        body = {
            "name": self.job_name
        }
        endpoint = f"{self.builder_endpoint}{consts.METASPONSE_ADD_JOB_METADATA}"
        ret_val, response = self._connector.util.make_rest_call(endpoint, self._action_result, method="post", data=body, headers={})

        if phantom.is_fail(ret_val):
            if phantom.is_fail(self.delete_builder()):
                return self._action_result.get_status()
            return self._action_result.get_status()

        return phantom.APP_SUCCESS

    def add_plugins(self):
        endpoint = f"{self.builder_endpoint}{consts.METASPONSE_ADD_PLUGIN}"
        for plugin in self.plugins:
            body = {
                "plugin_id": plugin
            }
            ret_val, _ = self._connector.util.make_rest_call(endpoint, self._action_result, method="post", data=body,
                                                                     headers={})
            if phantom.is_fail(ret_val):
                return self._action_result.get_status()

        return phantom.APP_SUCCESS

    def add_options(self):
        for key, value in self.job_options_dict.items():
            endpoint = f"{self.builder_endpoint}{consts.METASPONSE_ADD_OPTIONS.format(option_id=key)}"
            body = {
                "value": value
            }
            ret_val, response = self._connector.util.make_rest_call(endpoint, self._action_result, method="post", data=body,
                                                                     headers={})
            if phantom.is_fail(ret_val):
                return self._action_result.get_status()

            if response.get("validation_errors"):
                self.resp_json["error"] = response.get("validation_errors")
                self._action_result.add_data(self.resp_json)
                return self._action_result.set_status(phantom.APP_ERROR, "Error occurred for option id: {}".format(key))
        return phantom.APP_SUCCESS

    def check_job_status(self):
        endpoint = f"{self.builder_endpoint}{consts.METASPONSE_CHECK_JOB_STATUS}"
        ret_val, response = self._connector.util.make_rest_call(endpoint, self._action_result, headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        if not response.get("is_ready", False):
            self._action_result.add_data(response)
            return self._action_result.set_status(phantom.APP_ERROR,
                                                  "Unable to create job, Error: {}".format(response.get("error_msg")))

        self.resp_json["builder_id"] = self.builder_id
        self.resp_json["name"] = self.job_name
        self.resp_json["plugins"] = response.get("plugin_order")
        self.resp_json["options"] = self.job_options_dict
        self._action_result.add_data(self.resp_json)
        return phantom.APP_SUCCESS

    def delete_builder(self):
        endpoint = f'{consts.METASPONSE_BUILDER_ENDPOINT.format(builder_id=self.builder_id)}{".json"}'

        ret_val, _ = self._connector.util.make_rest_call(endpoint, self._action_result, method="delete", headers={})
        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        return phantom.APP_SUCCESS

    def execute(self):
        """Execute the create job action."""

        # initialize all job params
        if phantom.is_fail(self.initialize_params()):
            return self._action_result.get_status()

        # create and naming a job
        if phantom.is_fail(self.create_job()):
            return self._action_result.get_status()

        # adding plugins for newly created job
        if phantom.is_fail(self.add_plugins()):
            if phantom.is_fail(self.delete_builder()):
                return self._action_result.get_status()
            return self._action_result.get_status()

        # adding options for added plugins
        if phantom.is_fail(self.add_options()):
            if phantom.is_fail(self.delete_builder()):
                return self._action_result.get_status()
            return self._action_result.get_status()

        # check job status for any error
        if phantom.is_fail(self.check_job_status()):
            if phantom.is_fail(self.delete_builder()):
                return self._action_result.get_status()
            return self._action_result.get_status()

        return self._action_result.set_status(phantom.APP_SUCCESS, consts.METASPONSE_JOB_CREATED_MESSAGE)

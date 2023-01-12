# File: metasponse_connector.py
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

from __future__ import print_function, unicode_literals

import json

# Phantom App imports
import phantom.app as phantom
# Usage of the consts file is recommended
import requests
from phantom.base_connector import BaseConnector

from actions.metasponse_create_job import CreateJob
from actions.metasponse_get_all_jobs import GetAllJobs
from actions.metasponse_get_job_status import JobStatus
from actions.metasponse_job_control import JobControl
from actions.metasponse_kill_job import KillJob
from actions.metasponse_list_plugins import ListPlugins
from actions.metasponse_run_job import RunJob
from actions.metasponse_test_connectivity import TestConnectivityAction
from metasponse_utils import MetasponseUtils


class RetVal(tuple):

    def __new__(cls, val1, val2=None):
        return tuple.__new__(RetVal, (val1, val2))


class MetasponseConnector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(MetasponseConnector, self).__init__()

        self._state = None
        self.util = None
        self.config = None
        self.header = None

    def _handle_test_connectivity(self, param):
        """Create a test connectivity object and executes the action."""
        self.debug_print("In action handle for", self.get_action_identifier())

        action = TestConnectivityAction(self, param)
        return action.execute()

    def _handle_create_job(self, param):
        """Create a create job object and executes the action."""
        self.debug_print("In action handle for", self.get_action_identifier())

        action = CreateJob(self, param)
        return action.execute()

    def _handle_get_all_jobs(self, param):
        """Create a get all jobs object and executes the action."""
        self.debug_print("In action handle for", self.get_action_identifier())

        action = GetAllJobs(self, param)
        return action.execute()

    def _handle_run_job(self, param):
        """Create a run job object and executes the action."""
        self.debug_print("In action handle for", self.get_action_identifier())

        action = RunJob(self, param)
        return action.execute()

    def _handle_job_control(self, param):
        """Create a job control object and executes the action."""
        self.debug_print("In action handle for", self.get_action_identifier())

        action = JobControl(self, param)
        return action.execute()

    def _handle_get_job_status(self, param):
        """Create a job status object and executes the action."""

        self.debug_print("In action handle for", self.get_action_identifier())

        action = JobStatus(self, param)
        return action.execute()

    def _handle_kill_job(self, param):
        """Create a kill job object and executes the action."""

        self.debug_print("In action handle for", self.get_action_identifier())

        action = KillJob(self, param)
        return action.execute()

    def _handle_list_plugins(self, param):
        """Create a list plugins object and executes the action."""

        self.debug_print("In action handle for", self.get_action_identifier())

        action = ListPlugins(self, param)
        return action.execute()

    def handle_action(self, param):

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())
        actions = {
            "test_connectivity": self._handle_test_connectivity,
            "get_all_jobs": self._handle_get_all_jobs,
            "run_job": self._handle_run_job,
            "job_control": self._handle_job_control,
            "get_job_status": self._handle_get_job_status,
            "kill_job": self._handle_kill_job,
            "create_job": self._handle_create_job,
            "list_plugins": self._handle_list_plugins
        }
        if action_id in actions:
            return actions[action_id](param)

        self.debug_print("Action not implemented")
        return phantom.APP_ERROR

    def initialize(self):
        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        # Create the util object and use it throughout the action lifecycle
        self.util = MetasponseUtils(self)
        # get the asset config
        self.config = self.get_config()

        return phantom.APP_SUCCESS

    def finalize(self):
        # Save the state, this data is saved across actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


def main():  # pragma: no cover
    import argparse

    argparser = argparse.ArgumentParser()

    argparser.add_argument('input_test_json', help='Input Test JSON file')
    argparser.add_argument('-u', '--username', help='username', required=False)
    argparser.add_argument('-p', '--password', help='password', required=False)
    argparser.add_argument('-v', '--verify', action='store_true', help='verify', required=False, default=False)

    args = argparser.parse_args()
    session_id = None

    username = args.username
    password = args.password
    verify = args.verify

    if username is not None and password is None:

        # User specified a username but not a password, so ask
        import getpass
        password = getpass.getpass("Password: ")

    if username and password:
        try:
            login_url = MetasponseConnector._get_phantom_base_url() + '/login'

            print("Accessing the Login page")
            r = requests.get(login_url, verify=verify)
            csrftoken = r.cookies['csrftoken']

            data = dict()
            data['username'] = username
            data['password'] = password
            data['csrfmiddlewaretoken'] = csrftoken

            headers = dict()
            headers['Cookie'] = 'csrftoken=' + csrftoken
            headers['Referer'] = login_url

            print("Logging into Platform to get the session id")
            r2 = requests.post(login_url, verify=verify, data=data, headers=headers)
            session_id = r2.cookies['sessionid']
        except Exception as e:
            print("Unable to get session id from the platform. Error: " + str(e))
            exit(1)

    with open(args.input_test_json) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = MetasponseConnector()
        connector.print_progress_message = True

        if session_id is not None:
            in_json['user_session_token'] = session_id
            connector._set_csrf_info(csrftoken, headers['Referer'])

        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    exit(0)


if __name__ == '__main__':
    main()

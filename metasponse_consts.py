# File: metasponse_consts.py
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

METASPONSE_ERROR_ZERO_INT_PARAM = "Please provide a non-zero positive integer value in the '{key}' parameter"
METASPONSE_ERROR_INVALID_INT_PARAM = "Please provide a valid integer value in the '{key}' parameter"
METASPONSE_ERROR_INVALID_ACTION_PARAM = "Please provide a valid value in the '{key}' parameter"
METASPONSE_EMPTY_RESPONSE_STATUS_CODES = [200, 204]

# endpoints
METASPONSE_BUILDER_ENDPOINT = "/api/v1/builders/{builder_id}"
METASPONSE_CREATE_JOB = "/api/v1/builders.json"
METASPONSE_GET_ALL_JOBS = "/api/v1/jobs.json"
METASPONSE_RUN_JOB = "/api/v1/builders/{builder_id}.json"
METASPONSE_PICK_UP_JOB_GET_JOB_STATUS = "/api/v1/jobs/{job_name}/status.json"
METASPONSE_KILL_JOB = "/api/v1/jobs/{job_name}.json"
METASPONSE_ADD_PLUGIN = "/plugins.json"
METASPONSE_ADD_OPTIONS = "/options/{option_id}.json"
METASPONSE_ADD_JOB_METADATA = "/metadata.json"
METASPONSE_CHECK_JOB_STATUS = "/check.json"
METASPONSE_LIST_PLUGINS = "/api/v1/plugins.json"

# messages
METASPONSE_SUCCESS_TEST_CONNECTIVITY = "Test Connectivity Passed"
METASPONSE_ERROR_TEST_CONNECTIVITY = "Test Connectivity Failed"
METASPONSE_PICKUP_ABORT_JOB_MESSAGE = "Action {action} has been applied successfully on job"
METASPONSE_JOB_SCHEDULED_MESSAGE = "Job has been scheduled/deployed successfully"
METASPONSE_JOB_TEMPLATE_MESSAGE = "Job has been saved as a template"
METASPONSE_JOB_STATUS_MESSAGE = "Job status has been fetched successfully"
METASPONSE_KILL_JOB_MESSAGE = "Job has been deleted successfully"
METASPONSE_ERROR_MESSAGE_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters"
METASPONSE_ERROR_JSON_PARSE = "Unable to parse JSON for \'{}\' parameter"
METASPONSE_JOB_CREATED_MESSAGE = "Job has been created successfully, Use the builder id for run the job"
METASPONSE_ERROR_GENERAL_MESSAGE = "Status code: {0}, Data from server: {1}"
METASPONSE_ERROR_HTML_RESPONSE = "Error parsing html response"
METASPONSE_JOB_STATUS_ERROR_MESSAGE = "Job not found or job is not currently executing"

METASPONSE_REQUEST_DEFAULT_TIMEOUT = 30

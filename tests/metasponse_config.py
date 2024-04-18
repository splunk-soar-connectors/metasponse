# File: metasponse_config.py
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
CONTENT_TYPE = "application/json"
DEFAULT_ASSET_ID = "20000"
DEFAULT_HEADERS = {"Content-Type": CONTENT_TYPE}
TEST_JSON = {
    "action": "<action name>",
    "identifier": "<action_name>",
    "asset_id": DEFAULT_ASSET_ID,
    "config": {
        "appname": "-",
        "directory": "metasponse-e6d648b5-e80e-4d07-854c-26556cc23b33",
        "base_url": "https://base_url",
        "main_module": "metasponse_connector.py"
    },
    "debug_level": 3,
    "dec_key": DEFAULT_ASSET_ID,
    "parameters": [{}]
}

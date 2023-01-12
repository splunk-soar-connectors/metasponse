# File: __init__.py
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

from phantom.action_result import ActionResult


class BaseAction:
    """Base Action class to generate the action objects."""
    def __init__(self, connector, param):
        """Prepare constructor for actions.

        :param connector: Vision connector object
        :param param: Parameter dictionary
        """
        self._connector = connector
        self._action_result = connector.add_action_result(ActionResult(dict(param)))
        self._param = param

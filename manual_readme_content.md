[comment]: # "File: README.md"
[comment]: # "Copyright (c) 2023 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## Port Details

App supports **5003** port by default and it can be configured.

### Steps to run **create job** action

Parameters: **Job name** , **Job plugins** , **Job options**

1.  Add Job name.
2.  Add required plugins, check all available plugins by running **list plugins** action.
3.  For given plugins in **job plugins** parameter there must be some required options which have to
    provide in **job options** parameter  
    i.e **job.rhost** option is required option for creating any job, you need to provide your
    remote host value in job options.  
    for **ais.transports.ssh** plugin **ssh.user** , **ssh.password** is required option ids, you
    can check all options from **list plugins** action.  
4.  After adding the required options, Run the action.

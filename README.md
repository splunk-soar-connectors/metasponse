[comment]: # "Auto-generated SOAR connector documentation"
# Metasponse

Publisher: Splunk  
Connector Version: 1.0.2  
Product Vendor: AIS  
Product Name: Metasponse  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.5.0  

Connects to Metasponse platform using Metasponse API services

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


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Metasponse asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** |  required  | string | Base URL (example: https://myip:5003)
**verify_server_cert** |  optional  | boolean | Verify server certificate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[create job](#action-create-job) - Create a job with provided plugins and options  
[get all jobs](#action-get-all-jobs) - Get information of all deployed jobs  
[run job](#action-run-job) - Run or schedule a job using builder id, which is created from create job action  
[job control](#action-job-control) - Pickup or abort the job that is currently running on the platform  
[get job status](#action-get-job-status) - Get job status with all job properties  
[kill job](#action-kill-job) - Delete a job which is configured on platform  
[list plugins](#action-list-plugins) - Get information about all plugins  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'create job'
Create a job with provided plugins and options

Type: **generic**  
Read only: **False**

For job options, use the following format in "job_options" parameter<br>{ "ssh.user":"testuser", "ssh.password":"testpass", "job.rhost":"8.8.8.8" }.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_name** |  required  | Job name for creation | string |  `metasponse job name` 
**job_plugins** |  required  | Comma-separated plugin values | string |  `metasponse job plugins` 
**job_options** |  required  | Json string key-value pairs containing options and their values | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_name | string |  `metasponse job name`  |   test-job 
action_result.parameter.job_options | string |  |   { "ssh.user":"testuser", "ssh.password":"testpass", "job.rhost":"8.8.8.8" } 
action_result.parameter.job_plugins | string |  `metasponse job plugins`  |   ais.transports.ssh,ais.collectors.logins 
action_result.data.\*.builder_id | string |  `metasponse job builder id`  |   r4ed5295-d95c-4gae-896r5-895594c3c66f 
action_result.data.\*.name | string |  `metasponse job name`  |   test-job 
action_result.data.\*.options | string |  |  
action_result.data.\*.plugins | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Job has been created successfully, Use the builder id for run the job 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get all jobs'
Get information of all deployed jobs

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.data.\*._id | string |  |   83b51c76g691721e60d234vf 
action_result.data.\*.completion_token | string |  |   c52240a5-26w1-4rf1-9f40-3q44f4395zrf05 
action_result.data.\*.host_count | numeric |  |   1 
action_result.data.\*.iv | string |  |   Ge2FF1UOmbaF4LzIt6XPxN== 
action_result.data.\*.last_update | numeric |  |   1672814551.536 
action_result.data.\*.metrics.analysis.enabled | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.end_time | numeric |  |   1672843351.522606 
action_result.data.\*.metrics.analysis.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.runtime | numeric |  |   0.038991 
action_result.data.\*.metrics.analysis.start_time | numeric |  |   1672843351.483615 
action_result.data.\*.metrics.analysis_progress | numeric |  |   1 
action_result.data.\*.metrics.collection_coverage | numeric |  |   353 
action_result.data.\*.metrics.deployment.bandwidth | numeric |  |   45.47 
action_result.data.\*.metrics.deployment.enabled | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.end_time | numeric |  |   168.87 
action_result.data.\*.metrics.deployment.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.hosts_completed | numeric |  |   1 
action_result.data.\*.metrics.deployment.hosts_requiring_pickup | numeric |  |   1 
action_result.data.\*.metrics.deployment.hosts_with_errors | numeric |  |   1 
action_result.data.\*.metrics.deployment.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.pushed_files.average_file_size | numeric |  |   6236.5 
action_result.data.\*.metrics.deployment.pushed_files.file_count | numeric |  |   4 
action_result.data.\*.metrics.deployment.pushed_files.file_size | numeric |  |   24946 
action_result.data.\*.metrics.deployment.runtime | numeric |  |   5.12715 
action_result.data.\*.metrics.deployment.seconds_per_host | numeric |  |   5.12715 
action_result.data.\*.metrics.deployment.start_time | numeric |  |   1672842483.748148 
action_result.data.\*.metrics.deployment.targets.alive | numeric |  |   1 
action_result.data.\*.metrics.deployment.targets.dead | numeric |  |  
action_result.data.\*.metrics.deployment.targets.duplicate | numeric |  |   1 
action_result.data.\*.metrics.deployment.targets.excluded | numeric |  |   1 
action_result.data.\*.metrics.deployment.targets.total | numeric |  |   1 
action_result.data.\*.metrics.deployment_etc | numeric |  |   3 
action_result.data.\*.metrics.deployment_progress | numeric |  |   1 
action_result.data.\*.metrics.end_time | numeric |  |   1672843351.522606 
action_result.data.\*.metrics.expect_collections.\*.collection_name | string |  |   logins 
action_result.data.\*.metrics.expect_collections.\*.count | numeric |  |   1 
action_result.data.\*.metrics.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.bandwidth | numeric |  |   1 
action_result.data.\*.metrics.pickup.data_files.average_file_size | numeric |  |   134 
action_result.data.\*.metrics.pickup.data_files.file_count | numeric |  |   1 
action_result.data.\*.metrics.pickup.data_files.file_size | numeric |  |   1434 
action_result.data.\*.metrics.pickup.enabled | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.end_time | numeric |  |   163.034 
action_result.data.\*.metrics.pickup.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.hosts_completed | numeric |  |   1 
action_result.data.\*.metrics.pickup.hosts_with_errors | numeric |  |   1 
action_result.data.\*.metrics.pickup.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.runtime | numeric |  |   91.17933 
action_result.data.\*.metrics.pickup.seconds_per_host | numeric |  |   90.17937 
action_result.data.\*.metrics.pickup.start_time | numeric |  |   1672842542.908834 
action_result.data.\*.metrics.pickup.targets.alive | numeric |  |   1 
action_result.data.\*.metrics.pickup.targets.dead | numeric |  |  
action_result.data.\*.metrics.pickup.targets.duplicate | numeric |  |   1 
action_result.data.\*.metrics.pickup.targets.excluded | numeric |  |   4 
action_result.data.\*.metrics.pickup.targets.total | numeric |  |   1 
action_result.data.\*.metrics.pickup_etc | numeric |  |   1 
action_result.data.\*.metrics.pickup_progress | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.failure.average_runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.failure.count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.failure.runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.success.average_runtime | numeric |  |   0.001114133333325255 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.success.count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.success.runtime | numeric |  |   0.003342399999975765 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.total_count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.total_runtime | numeric |  |   0.003342399999975765 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.average_file_size | numeric |  |   21808 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.failure.average_runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.failure.count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.failure.runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.file_count | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.file_size | numeric |  |   21808 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.success.average_runtime | numeric |  |   0.005666000000000171 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.success.count | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.success.runtime | numeric |  |   0.005666000000000171 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.total_count | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.total_runtime | numeric |  |   0.005666000000000171 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.average_file_size | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.errors | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.file_count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.file_size | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.plugin_id | string |  |   ais.collectors.logins 
action_result.data.\*.metrics.plugin_metrics.\*.plugin_version | string |  |   1.5.0 
action_result.data.\*.metrics.plugin_metrics.\*.task.failure.average_runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.failure.count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.failure.runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.success.average_runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.success.count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.success.runtime | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.total_count | numeric |  |   3 
action_result.data.\*.metrics.plugin_metrics.\*.task.total_runtime | numeric |  |   3 
action_result.data.\*.metrics.progress | numeric |  |   1 
action_result.data.\*.metrics.runtime | numeric |  |   0.041986 
action_result.data.\*.metrics.start_time | numeric |  |   1672843351.48062 
action_result.data.\*.metrics.target_count | numeric |  |   1 
action_result.data.\*.name | string |  `metasponse job name`  |   test_job 
action_result.data.\*.operator.id | string |  |  
action_result.data.\*.operator.login | string |  |   APP\\Administrator 
action_result.data.\*.operator.name | string |  |   Administrator 
action_result.data.\*.options.\*.id | string |  |   plugins.debug 
action_result.data.\*.options.\*.salt | string |  |   LqLewPp9Lkea3IKrkw9fvf4== 
action_result.data.\*.options.\*.secure | boolean |  |   True  False 
action_result.data.\*.options.\*.value | boolean |  |   True  False 
action_result.data.\*.parent_id | string |  |  
action_result.data.\*.plugins.\*.id | string |  |   ais.collectors.logins 
action_result.data.\*.plugins.\*.version | string |  |   1.5.0 
action_result.data.\*.schedule_id | string |  |  
action_result.data.\*.start_token | string |  |   e1202445fb3-8fsa-4re6-b7d0-8dcn73654b 
action_result.data.\*.state | string |  |   completed  await-pickup  scheduled 
action_result.data.\*.task | boolean |  |   True  False 
action_result.data.\*.template | boolean |  |   True  False 
action_result.data.\*.version | string |  |   1.6.4.0 
action_result.summary | string |  |  
action_result.message | string |  |   Total job: 9 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'run job'
Run or schedule a job using builder id, which is created from create job action

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**builder_id** |  required  | Job builder ID | string |  `metasponse job builder id` 
**template** |  optional  | Save a job as a template | boolean | 
**delta** |  optional  | Schedules a builder using relative time (in seconds) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.builder_id | string |  `metasponse job builder id`  |   r4ed5295-d95c-4gae-896r5-895594c3c66f 
action_result.parameter.delta | numeric |  |   10 
action_result.parameter.template | boolean |  |   True  False 
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Job has been scheduled/deployed successfully 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'job control'
Pickup or abort the job that is currently running on the platform

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_name** |  required  | Job name for pickup or abort | string |  `metasponse job name` 
**action** |  required  | Action to perform on job | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.action | string |  |   pickup  abort 
action_result.parameter.job_name | string |  `metasponse job name`  |   test-job 
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Action pickup has been applied on job successfully 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get job status'
Get job status with all job properties

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_name** |  required  | Job name for get the status | string |  `metasponse job name` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_name | string |  `metasponse job name`  |   test-job 
action_result.data.\*.metrics.analysis.enabled | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.end_time | numeric |  |   23424.23 
action_result.data.\*.metrics.analysis.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.analysis.runtime | numeric |  |   43 
action_result.data.\*.metrics.analysis.start_time | numeric |  |   223.4 
action_result.data.\*.metrics.analysis_progress | numeric |  |   23 
action_result.data.\*.metrics.collection_coverage | numeric |  |   2 
action_result.data.\*.metrics.deployment.bandwidth | numeric |  |   34.22 
action_result.data.\*.metrics.deployment.enabled | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.end_time | numeric |  |   34.43 
action_result.data.\*.metrics.deployment.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.hosts_completed | numeric |  |   2 
action_result.data.\*.metrics.deployment.hosts_requiring_pickup | numeric |  |   2 
action_result.data.\*.metrics.deployment.hosts_with_errors | numeric |  |   2 
action_result.data.\*.metrics.deployment.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.deployment.pushed_files.average_file_size | numeric |  |   1231 
action_result.data.\*.metrics.deployment.pushed_files.file_count | numeric |  |   2323 
action_result.data.\*.metrics.deployment.pushed_files.file_size | numeric |  |   223 
action_result.data.\*.metrics.deployment.runtime | numeric |  |   4324.243 
action_result.data.\*.metrics.deployment.seconds_per_host | numeric |  |   2 
action_result.data.\*.metrics.deployment.start_time | numeric |  |   23.42 
action_result.data.\*.metrics.deployment.targets.alive | numeric |  |   2 
action_result.data.\*.metrics.deployment.targets.dead | numeric |  |   2 
action_result.data.\*.metrics.deployment.targets.duplicate | numeric |  |   2 
action_result.data.\*.metrics.deployment.targets.excluded | numeric |  |   2 
action_result.data.\*.metrics.deployment.targets.total | numeric |  |   2 
action_result.data.\*.metrics.deployment_etc | numeric |  |   3434 
action_result.data.\*.metrics.deployment_progress | numeric |  |   2 
action_result.data.\*.metrics.end_time | numeric |  |   1673447475.244199 
action_result.data.\*.metrics.expect_collections.\*.collection_name | string |  |   logins 
action_result.data.\*.metrics.expect_collections.\*.count | numeric |  |   1 
action_result.data.\*.metrics.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.bandwidth | numeric |  |   24 
action_result.data.\*.metrics.pickup.data_files.average_file_size | numeric |  |   234 
action_result.data.\*.metrics.pickup.data_files.file_count | numeric |  |   4 
action_result.data.\*.metrics.pickup.data_files.file_size | numeric |  |   223 
action_result.data.\*.metrics.pickup.enabled | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.end_time | string |  |   22323 
action_result.data.\*.metrics.pickup.has_completed | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.has_started | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.hosts_completed | numeric |  |   2 
action_result.data.\*.metrics.pickup.hosts_with_errors | numeric |  |   3 
action_result.data.\*.metrics.pickup.is_active | boolean |  |   True  False 
action_result.data.\*.metrics.pickup.runtime | numeric |  |   2 
action_result.data.\*.metrics.pickup.seconds_per_host | numeric |  |   232 
action_result.data.\*.metrics.pickup.start_time | string |  |   2244 
action_result.data.\*.metrics.pickup.targets.alive | numeric |  |   2 
action_result.data.\*.metrics.pickup.targets.dead | numeric |  |   2 
action_result.data.\*.metrics.pickup.targets.duplicate | numeric |  |   2 
action_result.data.\*.metrics.pickup.targets.excluded | numeric |  |   2 
action_result.data.\*.metrics.pickup.targets.total | numeric |  |   2 
action_result.data.\*.metrics.pickup_etc | numeric |  |   2 
action_result.data.\*.metrics.pickup_progress | numeric |  |   234 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.failure.average_runtime | numeric |  |   2345.3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.failure.count | numeric |  |   34 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.failure.runtime | numeric |  |   234.3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.success.average_runtime | numeric |  |   234.3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.success.count | numeric |  |   2 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.success.runtime | numeric |  |   34.32 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.total_count | numeric |  |   34.3 
action_result.data.\*.metrics.plugin_metrics.\*.analysis.total_runtime | numeric |  |   234.3 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.average_file_size | numeric |  |   21808 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.failure.average_runtime | numeric |  |   223.4 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.failure.count | numeric |  |   2 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.failure.runtime | numeric |  |   234.2 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.file_count | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.file_size | numeric |  |   21808 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.success.average_runtime | numeric |  |   0.004861800000000027 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.success.count | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.success.runtime | numeric |  |   0.004861800000000027 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.total_count | numeric |  |   1 
action_result.data.\*.metrics.plugin_metrics.\*.deployment.total_runtime | numeric |  |   0.004861800000000027 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.average_file_size | numeric |  |   43 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.errors | numeric |  |   2 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.file_count | numeric |  |   2 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.file_size | numeric |  |   244 
action_result.data.\*.metrics.plugin_metrics.\*.pickup.runtime | numeric |  |   2 
action_result.data.\*.metrics.plugin_metrics.\*.plugin_id | string |  |   ais.collectors.logins 
action_result.data.\*.metrics.plugin_metrics.\*.plugin_version | string |  |   1.5.0 
action_result.data.\*.metrics.plugin_metrics.\*.task.failure.average_runtime | numeric |  |   5 
action_result.data.\*.metrics.plugin_metrics.\*.task.failure.count | numeric |  |   2 
action_result.data.\*.metrics.plugin_metrics.\*.task.failure.runtime | numeric |  |   4 
action_result.data.\*.metrics.plugin_metrics.\*.task.success.average_runtime | numeric |  |   24.5 
action_result.data.\*.metrics.plugin_metrics.\*.task.success.count | numeric |  |   5 
action_result.data.\*.metrics.plugin_metrics.\*.task.success.runtime | numeric |  |   234.3 
action_result.data.\*.metrics.plugin_metrics.\*.task.total_count | numeric |  |   234.23 
action_result.data.\*.metrics.plugin_metrics.\*.task.total_runtime | numeric |  |   2434.4 
action_result.data.\*.metrics.progress | numeric |  |   2 
action_result.data.\*.metrics.runtime | numeric |  |   2324 
action_result.data.\*.metrics.start_time | numeric |  |   223.23 
action_result.data.\*.metrics.target_count | numeric |  |   1 
action_result.data.\*.pickup_only | boolean |  |   True  False 
action_result.data.\*.pid | string |  |   2345 
action_result.data.\*.state | string |  |   completed  await-pickup  scheduled  aborted 
action_result.data.\*.target_count | numeric |  |   1 
action_result.data.\*.wakeup_time | numeric |  |   223.23 
action_result.data.\*.worker_count | numeric |  |   1 
action_result.summary | string |  |  
action_result.message | string |  |   Get the job status successfully 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'kill job'
Delete a job which is configured on platform

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_name** |  required  | Job name for delete | string |  `metasponse job name` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_name | string |  `metasponse job name`  |   test-job 
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Job has been deleted successfully 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list plugins'
Get information about all plugins

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.data.\*.altitude | numeric |  |   10100 
action_result.data.\*.altitude_option_id | string |  |   altitude.analyzer.alienvault 
action_result.data.\*.author | string |  |   Metasponse Team 
action_result.data.\*.builtin | boolean |  |   True  False 
action_result.data.\*.description | string |  |   AlienValue Analyzer 
action_result.data.\*.email | string |  |   testurl@gmail.com 
action_result.data.\*.id | string |  `metasponse job plugins`  |   ais.analyzers.alienvault 
action_result.data.\*.indexes | string |  |  
action_result.data.\*.name | string |  |   AlienVault Analyzer 
action_result.data.\*.options.\*.category | string |  |   Plugin Reporting 
action_result.data.\*.options.\*.choices | string |  |  
action_result.data.\*.options.\*.default | string |  |   ~ 
action_result.data.\*.options.\*.description | string |  |   Destination directory for Plugin reports 
action_result.data.\*.options.\*.id | string |  |   alienvault.outdir 
action_result.data.\*.options.\*.name | string |  |   Plugin: Output Directory 
action_result.data.\*.options.\*.required | boolean |  |   True  False 
action_result.data.\*.options.\*.secure | boolean |  |   True  False 
action_result.data.\*.options.\*.topic | string |  |  
action_result.data.\*.options.\*.type | string |  |   str 
action_result.data.\*.path | string |  |   analyzers/alienvault 
action_result.data.\*.requires_escalation | boolean |  |   True  False 
action_result.data.\*.task | boolean |  |   True  False 
action_result.data.\*.topic | string |  |  
action_result.data.\*.type | string |  |   analyzer 
action_result.data.\*.version | string |  |   1.0.0 
action_result.summary | string |  |  
action_result.message | string |  |   Total plugins: 9 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
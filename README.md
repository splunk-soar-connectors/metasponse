[comment]: # "Auto-generated SOAR connector documentation"
# Metasponse

Publisher: Splunk  
Connector Version: 1\.0\.0  
Product Vendor: AIS  
Product Name: Metasponse  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.5\.0  

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
**base\_url** |  required  | string | Base URL \(example\: https\://myip\:5003\)
**verify\_server\_cert** |  optional  | boolean | Verify server certificate

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

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_name** |  required  | Job name for creation | string |  `metasponse job name` 
**job\_plugins** |  required  | Comma\-separated plugin values | string | 
**job\_options** |  required  | Json string key\-value pairs containing options and their values | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_name | string |  `metasponse job name`  |   test\-job 
action\_result\.parameter\.job\_options | string |  |   \{ "ssh\.user"\:"testuser", "ssh\.password"\:"testpass", "job\.rhost"\:"8\.8\.8\.8" \} 
action\_result\.parameter\.job\_plugins | string |  |   ais\.transports\.ssh,ais\.collectors\.logins 
action\_result\.data\.\*\.builder\_id | string |  `metasponse job builder id`  |   r4ed5295\-d95c\-4gae\-896r5\-895594c3c66f 
action\_result\.data\.\*\.name | string |  `metasponse job name`  |   test\-job 
action\_result\.data\.\*\.options | string |  |  
action\_result\.data\.\*\.plugins | string |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Job has been created successfully, Use the builder id for run the job 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'get all jobs'
Get information of all deployed jobs

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.data\.\*\.\_id | string |  |   83b51c76g691721e60d234vf 
action\_result\.data\.\*\.completion\_token | string |  |   c52240a5\-26w1\-4rf1\-9f40\-3q44f4395zrf05 
action\_result\.data\.\*\.host\_count | numeric |  |   1 
action\_result\.data\.\*\.iv | string |  |   Ge2FF1UOmbaF4LzIt6XPxN== 
action\_result\.data\.\*\.last\_update | numeric |  |   1672814551.536 
action\_result\.data\.\*\.metrics\.analysis\.enabled | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.end\_time | numeric |  |   1672843351.522606 
action\_result\.data\.\*\.metrics\.analysis\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.runtime | numeric |  |   0.038991 
action\_result\.data\.\*\.metrics\.analysis\.start\_time | numeric |  |   1672843351.483615 
action\_result\.data\.\*\.metrics\.analysis\_progress | numeric |  |   1 
action\_result\.data\.\*\.metrics\.collection\_coverage | numeric |  |   353 
action\_result\.data\.\*\.metrics\.deployment\.bandwidth | numeric |  |   45.47 
action\_result\.data\.\*\.metrics\.deployment\.enabled | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.end\_time | numeric |  |   168.87 
action\_result\.data\.\*\.metrics\.deployment\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.hosts\_completed | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\.hosts\_requiring\_pickup | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\.hosts\_with\_errors | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.pushed\_files\.average\_file\_size | numeric |  |   6236.5 
action\_result\.data\.\*\.metrics\.deployment\.pushed\_files\.file\_count | numeric |  |   4 
action\_result\.data\.\*\.metrics\.deployment\.pushed\_files\.file\_size | numeric |  |   24946 
action\_result\.data\.\*\.metrics\.deployment\.runtime | numeric |  |   5.12715 
action\_result\.data\.\*\.metrics\.deployment\.seconds\_per\_host | numeric |  |   5.12715 
action\_result\.data\.\*\.metrics\.deployment\.start\_time | numeric |  |   1672842483.748148 
action\_result\.data\.\*\.metrics\.deployment\.targets\.alive | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\.targets\.dead | numeric |  |  
action\_result\.data\.\*\.metrics\.deployment\.targets\.duplicate | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\.targets\.excluded | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\.targets\.total | numeric |  |   1 
action\_result\.data\.\*\.metrics\.deployment\_etc | numeric |  |   3 
action\_result\.data\.\*\.metrics\.deployment\_progress | numeric |  |   1 
action\_result\.data\.\*\.metrics\.end\_time | numeric |  |   1672843351.522606 
action\_result\.data\.\*\.metrics\.expect\_collections\.\*\.collection\_name | string |  |   logins 
action\_result\.data\.\*\.metrics\.expect\_collections\.\*\.count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.bandwidth | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\.data\_files\.average\_file\_size | numeric |  |   134 
action\_result\.data\.\*\.metrics\.pickup\.data\_files\.file\_count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\.data\_files\.file\_size | numeric |  |   1434 
action\_result\.data\.\*\.metrics\.pickup\.enabled | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.end\_time | numeric |  |   163.034 
action\_result\.data\.\*\.metrics\.pickup\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.hosts\_completed | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\.hosts\_with\_errors | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.runtime | numeric |  |   91.17933 
action\_result\.data\.\*\.metrics\.pickup\.seconds\_per\_host | numeric |  |   90.17937 
action\_result\.data\.\*\.metrics\.pickup\.start\_time | numeric |  |   1672842542.908834 
action\_result\.data\.\*\.metrics\.pickup\.targets\.alive | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\.targets\.dead | numeric |  |  
action\_result\.data\.\*\.metrics\.pickup\.targets\.duplicate | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\.targets\.excluded | numeric |  |   4 
action\_result\.data\.\*\.metrics\.pickup\.targets\.total | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\_etc | numeric |  |   1 
action\_result\.data\.\*\.metrics\.pickup\_progress | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.failure\.average\_runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.failure\.count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.failure\.runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.success\.average\_runtime | numeric |  |   0.001114133333325255 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.success\.count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.success\.runtime | numeric |  |   0.003342399999975765 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.total\_count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.total\_runtime | numeric |  |   0.003342399999975765 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.average\_file\_size | numeric |  |   21808 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.failure\.average\_runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.failure\.count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.failure\.runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.file\_count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.file\_size | numeric |  |   21808 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.success\.average\_runtime | numeric |  |   0.005666000000000171 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.success\.count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.success\.runtime | numeric |  |   0.005666000000000171 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.total\_count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.total\_runtime | numeric |  |   0.005666000000000171 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.average\_file\_size | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.errors | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.file\_count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.file\_size | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.plugin\_id | string |  |   ais\.collectors\.logins 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.plugin\_version | string |  |   1\.5\.0 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.failure\.average\_runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.failure\.count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.failure\.runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.success\.average\_runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.success\.count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.success\.runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.total\_count | numeric |  |   3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.total\_runtime | numeric |  |   3 
action\_result\.data\.\*\.metrics\.progress | numeric |  |   1 
action\_result\.data\.\*\.metrics\.runtime | numeric |  |   0.041986 
action\_result\.data\.\*\.metrics\.start\_time | numeric |  |   1672843351.48062 
action\_result\.data\.\*\.metrics\.target\_count | numeric |  |   1 
action\_result\.data\.\*\.name | string |  `metasponse job name`  |   test\_job 
action\_result\.data\.\*\.operator\.id | string |  |  
action\_result\.data\.\*\.operator\.login | string |  |   APP\\Administrator 
action\_result\.data\.\*\.operator\.name | string |  |   Administrator 
action\_result\.data\.\*\.options\.\*\.id | string |  |   plugins\.debug 
action\_result\.data\.\*\.options\.\*\.salt | string |  |   LqLewPp9Lkea3IKrkw9fvf4== 
action\_result\.data\.\*\.options\.\*\.secure | boolean |  |   True  False 
action\_result\.data\.\*\.options\.\*\.value | boolean |  |   True  False 
action\_result\.data\.\*\.parent\_id | string |  |  
action\_result\.data\.\*\.plugins\.\*\.id | string |  |   ais\.collectors\.logins 
action\_result\.data\.\*\.plugins\.\*\.version | string |  |   1\.5\.0 
action\_result\.data\.\*\.schedule\_id | string |  |  
action\_result\.data\.\*\.start\_token | string |  |   e1202445fb3\-8fsa\-4re6\-b7d0\-8dcn73654b 
action\_result\.data\.\*\.state | string |  |   completed  await\-pickup  scheduled 
action\_result\.data\.\*\.task | boolean |  |   True  False 
action\_result\.data\.\*\.template | boolean |  |   True  False 
action\_result\.data\.\*\.version | string |  |   1\.6\.4\.0 
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Total job\: 9 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'run job'
Run or schedule a job using builder id, which is created from create job action

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**builder\_id** |  required  | Job builder ID | string |  `metasponse job builder id` 
**template** |  optional  | Save a job as a template | boolean | 
**delta** |  optional  | Schedules a builder using relative time \(in seconds\) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.builder\_id | string |  `metasponse job builder id`  |   r4ed5295\-d95c\-4gae\-896r5\-895594c3c66f 
action\_result\.parameter\.delta | numeric |  |   10 
action\_result\.parameter\.template | boolean |  |   True  False 
action\_result\.data | string |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Job has been scheduled/deployed successfully 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'job control'
Pickup or abort the job that is currently running on the platform

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_name** |  required  | Job name for pickup or abort | string |  `metasponse job name` 
**action** |  required  | Action to perform on job | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.action | string |  |   pickup  abort 
action\_result\.parameter\.job\_name | string |  `metasponse job name`  |   test\-job 
action\_result\.data | string |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Action pickup has been applied on job successfully 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'get job status'
Get job status with all job properties

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_name** |  required  | Job name for get the status | string |  `metasponse job name` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_name | string |  `metasponse job name`  |   test\-job 
action\_result\.data\.\*\.metrics\.analysis\.enabled | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.end\_time | numeric |  |   23424.23 
action\_result\.data\.\*\.metrics\.analysis\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.analysis\.runtime | numeric |  |   43 
action\_result\.data\.\*\.metrics\.analysis\.start\_time | numeric |  |   223.4 
action\_result\.data\.\*\.metrics\.analysis\_progress | numeric |  |   23 
action\_result\.data\.\*\.metrics\.collection\_coverage | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.bandwidth | numeric |  |   34.22 
action\_result\.data\.\*\.metrics\.deployment\.enabled | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.end\_time | numeric |  |   34.43 
action\_result\.data\.\*\.metrics\.deployment\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.hosts\_completed | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.hosts\_requiring\_pickup | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.hosts\_with\_errors | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.deployment\.pushed\_files\.average\_file\_size | numeric |  |   1231 
action\_result\.data\.\*\.metrics\.deployment\.pushed\_files\.file\_count | numeric |  |   2323 
action\_result\.data\.\*\.metrics\.deployment\.pushed\_files\.file\_size | numeric |  |   223 
action\_result\.data\.\*\.metrics\.deployment\.runtime | numeric |  |   4324.243 
action\_result\.data\.\*\.metrics\.deployment\.seconds\_per\_host | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.start\_time | numeric |  |   23.42 
action\_result\.data\.\*\.metrics\.deployment\.targets\.alive | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.targets\.dead | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.targets\.duplicate | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.targets\.excluded | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\.targets\.total | numeric |  |   2 
action\_result\.data\.\*\.metrics\.deployment\_etc | numeric |  |   3434 
action\_result\.data\.\*\.metrics\.deployment\_progress | numeric |  |   2 
action\_result\.data\.\*\.metrics\.end\_time | numeric |  |   1673447475.244199 
action\_result\.data\.\*\.metrics\.expect\_collections\.\*\.collection\_name | string |  |   logins 
action\_result\.data\.\*\.metrics\.expect\_collections\.\*\.count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.bandwidth | numeric |  |   24 
action\_result\.data\.\*\.metrics\.pickup\.data\_files\.average\_file\_size | numeric |  |   234 
action\_result\.data\.\*\.metrics\.pickup\.data\_files\.file\_count | numeric |  |   4 
action\_result\.data\.\*\.metrics\.pickup\.data\_files\.file\_size | numeric |  |   223 
action\_result\.data\.\*\.metrics\.pickup\.enabled | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.end\_time | string |  |   22323 
action\_result\.data\.\*\.metrics\.pickup\.has\_completed | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.has\_started | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.hosts\_completed | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\.hosts\_with\_errors | numeric |  |   3 
action\_result\.data\.\*\.metrics\.pickup\.is\_active | boolean |  |   True  False 
action\_result\.data\.\*\.metrics\.pickup\.runtime | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\.seconds\_per\_host | numeric |  |   232 
action\_result\.data\.\*\.metrics\.pickup\.start\_time | string |  |   2244 
action\_result\.data\.\*\.metrics\.pickup\.targets\.alive | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\.targets\.dead | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\.targets\.duplicate | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\.targets\.excluded | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\.targets\.total | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\_etc | numeric |  |   2 
action\_result\.data\.\*\.metrics\.pickup\_progress | numeric |  |   234 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.failure\.average\_runtime | numeric |  |   2345.3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.failure\.count | numeric |  |   34 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.failure\.runtime | numeric |  |   234.3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.success\.average\_runtime | numeric |  |   234.3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.success\.count | numeric |  |   2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.success\.runtime | numeric |  |   34.32 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.total\_count | numeric |  |   34.3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.analysis\.total\_runtime | numeric |  |   234.3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.average\_file\_size | numeric |  |   21808 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.failure\.average\_runtime | numeric |  |   223.4 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.failure\.count | numeric |  |   2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.failure\.runtime | numeric |  |   234.2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.file\_count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.file\_size | numeric |  |   21808 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.success\.average\_runtime | numeric |  |   0.004861800000000027 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.success\.count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.success\.runtime | numeric |  |   0.004861800000000027 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.total\_count | numeric |  |   1 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.deployment\.total\_runtime | numeric |  |   0.004861800000000027 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.average\_file\_size | numeric |  |   43 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.errors | numeric |  |   2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.file\_count | numeric |  |   2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.file\_size | numeric |  |   244 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.pickup\.runtime | numeric |  |   2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.plugin\_id | string |  |   ais\.collectors\.logins 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.plugin\_version | string |  |   1\.5\.0 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.failure\.average\_runtime | numeric |  |   5 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.failure\.count | numeric |  |   2 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.failure\.runtime | numeric |  |   4 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.success\.average\_runtime | numeric |  |   24.5 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.success\.count | numeric |  |   5 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.success\.runtime | numeric |  |   234.3 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.total\_count | numeric |  |   234.23 
action\_result\.data\.\*\.metrics\.plugin\_metrics\.\*\.task\.total\_runtime | numeric |  |   2434.4 
action\_result\.data\.\*\.metrics\.progress | numeric |  |   2 
action\_result\.data\.\*\.metrics\.runtime | numeric |  |   2324 
action\_result\.data\.\*\.metrics\.start\_time | numeric |  |   223.23 
action\_result\.data\.\*\.metrics\.target\_count | numeric |  |   1 
action\_result\.data\.\*\.pickup\_only | boolean |  |   True  False 
action\_result\.data\.\*\.pid | string |  |   2345 
action\_result\.data\.\*\.state | string |  |   completed  await\-pickup  scheduled  aborted 
action\_result\.data\.\*\.target\_count | numeric |  |   1 
action\_result\.data\.\*\.wakeup\_time | numeric |  |   223.23 
action\_result\.data\.\*\.worker\_count | numeric |  |   1 
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Get the job status successfully 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'kill job'
Delete a job which is configured on platform

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_name** |  required  | Job name for delete | string |  `metasponse job name` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_name | string |  `metasponse job name`  |   test\-job 
action\_result\.data | string |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Job has been deleted successfully 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'list plugins'
Get information about all plugins

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.data\.\*\.altitude | numeric |  |   10100 
action\_result\.data\.\*\.altitude\_option\_id | string |  |   altitude\.analyzer\.alienvault 
action\_result\.data\.\*\.author | string |  |   Metasponse Team 
action\_result\.data\.\*\.builtin | boolean |  |   True  False 
action\_result\.data\.\*\.description | string |  |   AlienValue Analyzer 
action\_result\.data\.\*\.email | string |  |   testurl\@gmail\.com 
action\_result\.data\.\*\.id | string |  `metasponse job plugins`  |   ais\.analyzers\.alienvault 
action\_result\.data\.\*\.indexes | string |  |  
action\_result\.data\.\*\.name | string |  |   AlienVault Analyzer 
action\_result\.data\.\*\.options\.\*\.category | string |  |   Plugin Reporting 
action\_result\.data\.\*\.options\.\*\.choices | string |  |  
action\_result\.data\.\*\.options\.\*\.default | string |  |   ~ 
action\_result\.data\.\*\.options\.\*\.description | string |  |   Destination directory for Plugin reports 
action\_result\.data\.\*\.options\.\*\.id | string |  |   alienvault\.outdir 
action\_result\.data\.\*\.options\.\*\.name | string |  |   Plugin\: Output Directory 
action\_result\.data\.\*\.options\.\*\.required | boolean |  |   True  False 
action\_result\.data\.\*\.options\.\*\.secure | boolean |  |   True  False 
action\_result\.data\.\*\.options\.\*\.topic | string |  |  
action\_result\.data\.\*\.options\.\*\.type | string |  |   str 
action\_result\.data\.\*\.path | string |  |   analyzers/alienvault 
action\_result\.data\.\*\.requires\_escalation | boolean |  |   True  False 
action\_result\.data\.\*\.task | boolean |  |   True  False 
action\_result\.data\.\*\.topic | string |  |   
    Analyze collected data against
    \[ref\]\(Plugin/task/sync/alienvault "synchronized Alienvault OTX pulses and indicators"\) and flag
    items that match a known IOC, such as file hash or IPv4 address\. 
action\_result\.data\.\*\.type | string |  |   analyzer 
action\_result\.data\.\*\.version | string |  |   1\.0\.0 
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Total plugins\: 9 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1 
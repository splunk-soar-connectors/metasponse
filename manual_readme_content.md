## Port Details

App supports **5003** port by default and it can be configured.

### Steps to run **create job** action

Parameters: **Job name** , **Job plugins** , **Job options**

1. Add Job name.
1. Add required plugins, check all available plugins by running **list plugins** action.
1. For given plugins in **job plugins** parameter there must be some required options which have to
   provide in **job options** parameter\
   i.e **job.rhost** option is required option for creating any job, you need to provide your
   remote host value in job options.\
   for **ais.transports.ssh** plugin **ssh.user** , **ssh.password** is required option ids, you
   can check all options from **list plugins** action.
1. After adding the required options, Run the action.

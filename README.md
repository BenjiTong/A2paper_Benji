# A2
A2 main project

## Quick start

### step 1. start and init the supervisor [ansible]

Install python, pip, virtualenv, and the requirements.

Scp the private key file, including both aws and ssh_key.

Modify the python path in "hosts" file.

Modify the war_dir in  "all" file.

### step 2. start the EC2 server: nginx * 2 + tomcat * 2 [ansible,EC2,ELB]

Run ansible to generate EC2 servers.

Delete the supervisor ip from "hosts" and "all" files.

### step 3. install nginx and tomcat and java server [ansible,EC2,NAT]

Java project need to be built before the deployment. apt install maven. mvn package.

Non-default subnet in aws would be no right to access internet. So you need NAT in this step.

### step 4. RDS mysql master configure [cloudformation,RDS,secrets_manager,Master-slave,lambda,autogenearte_password]

At region: us-east-1. B/c the S3 open data is on us-east-1.
Lambda codes need to be modified as the new mysql ip.

### step 5. RDS mysql slave configure [RDS]

Our main site is running at ap-southeast-1.

### step 6. deploy the lambda function && SQS to process the open data of S3 [lambda,SQS,CloudWatch,S3]

Run create.sql in master node. The crawler must be deployed to us-east-1, which is closed to S3 open data. Do note forget update the DB configuration.

Trigger the scrawler by a test message.

All of the result will be stored in mysql master endpoint.

URL is http://httpelb-1499061197.ap-southeast-1.elb.amazonaws.com/.

Running at Singapore IDC.

All above steps run by a IAM user [IAM].

[End]

# Details

## Directories introduction

deploy/  all the ansible project

paper/   all the latex files

java/    appserver

data/     data processor

## About git flow

To save times for us, using the commands like below：

```shell

git clone git@github.com:A2Inc/A2.git    # clone the project

git checkout -b ZC  # checkout and generate your own branch

vim thisisZC .... # coding with IDE you like

git commit -am 'update something'   # commit with the message 

git push origin ZC   # push to github

```

You only need to repeat the last three steps above and open the url https://github.com/A2Inc/A2/pulls to create a "pull request"

You also need to merge from main branch to update your own branch everyday:

```shell

$ git checkout main
$ git pull
$ checkout [YourBranchName]
$ git merge main

```

## Auto deploy

Ansible is used for the automatic deployment. Readme file is in the deploy directory.
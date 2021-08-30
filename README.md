# A2
A2 main project

## Quick start

step 1. start the supervisor server

13.229.208.228 is the public IP.

It could be forbidde by the GFW. Redo step 1 to get another IP.
It could be the Security Group reason. Ok, let's go to step2.

step 2. init the supervisor

The server is very slow from China mainland, so it is better that if you have a good oversea server to visit amazon IDC.

step 3. prepare the auto deployment envionment

There are lots of python pakcage needing to be installed.

Ensure the group_vars/all content do not contains : unused host ip.
Ensure the initial is true.
Ensure the python path is right.

step 4. start the EC2 server: nginx * 2 + tomcat * 2

In this step, 2 nginx EC2 and a ELB will be installed and 2 tomcat E2C will be ready.

step 5. install nginx and tomcat and java server

Fisrt of all, we need to check 2 of nginx and 2 of tomcat could be at the right position in hosts and all files.


















































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
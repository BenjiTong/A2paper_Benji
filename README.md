# A2
A2 main project

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
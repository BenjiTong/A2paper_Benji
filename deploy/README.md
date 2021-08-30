# How to deploy
## Quick start

Initial Environment

```shell

$pip3 install virtualenv
$virtualenv -p /usr/bin/python3 A2IncEnv
$source A2IncEnv/bin/activate
$(A2IncEnv) xx $ pip3 install -r requirements.txt

```

Initial Configuration

```shell

inventories/hosts: 
  ansible_python_interpreter=/Users/chenzhen/Documents/workspace/compx527/bin/python
group_vars/all:
  initial: true
  ec2_private_key_dir: "~/.ssh/cz_sg-ec2-key.pem" # modify to you own pem file
group_vars/all:

```
Initiall Running:

```shell

ansible-playbook -v -i hosts site.yml

```

Deploy:

```shell

update group_vars/all:
  initial: false

ansible-playbook -v -i hosts site.yml

```

read more information as below...

## tools requirements

```shell

$pip3 install virtualenv
$virtualenv -p /usr/bin/python3 A2IncEnv
$source A2IncEnv/bin/activate
$(A2IncEnv) xx $ pip3 install -r requirements.txt

```

## update the initial files

Modify the inventories/hosts:

```shell
 
  ansible_python_interpreter=/Users/chenzhen/Documents/workspace/compx527/bin/python

```

to your own directory.

## generate the EC2 server

Modify the group_vars/all:

```shell

initial: true
ec2_private_key_dir: "~/.ssh/cz_sg-ec2-key.pem" # modify to you own pem file

```

Then run the ansible-playbook:

```shell

ansible-playbook -v -i hosts site.yml

```

Be careful, you need to prepare the aws-cli environment at first. (You should run "aws configure".)

Totally, 4 EC2 instances could be generated after running. (nginx*2, tomcat*2)

## terminate the servers

To save the budget, after using them, dont forget termniating them.

Upate the group_vars/all:

```shell

initial: false
terminate: true

```

Run the ansible-playbook to terminate all your instances:

```shell

ansible-playbook -v -i hosts site.yml

```

## deploy 

Change both initial and terminal to false in "all".

Install and configure nginx:

```shell

ansible-playbook -v -i hosts site.yml -t nginx

```

Install and configure tomcat:

```shell

ansible-playbook -v -i hosts site.yml -t tomcat

```

## deploy java app

Download maven from here https://maven.apache.org/download.cgi?Preferred=ftp://ftp.osuosl.org/pub/apache/

Unzip the maven you will get the mvn command.

```shell

mvn package

```

modify group_vars/all to your own war_dir:

```shell

war_dir: "/Users/chenzhen/Documents/workspace/A2/java/target/web-0.0.1-SNAPSHOT/"

```

Deploy java app:

```shell

ansible-playbook -v -i hosts site.yml -t java

```

## start one single EC2:

```shell

ansible-playbook -v -i hosts supervisor.yml

```
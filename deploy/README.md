# How to deploy

## tools requirements

```shell

$pip3 install virtualenv
$virtualenv -p /usr/bin/python3 A2IncEnv
$source A2IncEnv/bin/activate
$(A2IncEnv) xx $ pip3 install -r requirements.txt

```

## update the initial files

Modify the inventories/hosts:

ansible_python_interpreter=/Users/chenzhen/Documents/workspace/compx527/bin/python

to your directory.

## generate the EC2 server

ansible-playbook main.yml -t provision -i inventories/hosts

Be careful, you need to prepare the aws-cli environment at first. (You should run "aws configure".)


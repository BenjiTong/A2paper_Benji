# The following parameters must be defined for yours
# installation. They may be set in a
# local deploy_parameters.make file
DEPLOY_BUCKET = a2-backup-sqs-sns

-include deploy_parameters.make

# Primary
APP = dbsm
STACK_NAME = dbsm

# Derived slave
SLAVE_TEMPLATE = $(APP)_template.yaml
SLAVE_PACKAGED = $(APP)_packaged_template.yaml

validate:
	aws cloudformation validate-template --template-body file://$(SLAVE_TEMPLATE)

package:
	aws cloudformation package --template-file $(SLAVE_TEMPLATE) --s3-bucket $(DEPLOY_BUCKET) --output-template $(SLAVE_PACKAGED) 

deploy: validate package
	aws cloudformation deploy --template-file $(SLAVE_PACKAGED) --stack-name $(STACK_NAME) --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM



# Derived master
MASTER_TEMPLATE = $(APP)_template_master.yaml
MASTER_PACKAGED = $(APP)_packaged_template_master.yaml

vmaster:
	aws cloudformation validate-template --template-body file://$(MASTER_TEMPLATE)

pmaster:
	aws cloudformation package --template-file $(MASTER_TEMPLATE) --s3-bucket $(DEPLOY_BUCKET) --output-template $(MASTER_PACKAGED) 

master: vmaster pmaster
	aws cloudformation deploy --template-file $(MASTER_PACKAGED) --stack-name $(STACK_NAME) --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM


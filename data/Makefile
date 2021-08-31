# The following parameters must be defined for yours
# installation. They may be set in a
# local deploy_parameters.make file
DEPLOY_BUCKET = a2-backup-sqs-sns-us

-include deploy_parameters.make

# Primary
APP = crawler
STACK_NAME = crawler

# Derived
TEMPLATE = $(APP)_template.yaml
PACKAGED = $(APP)_packaged_template.yaml

validate:
	aws cloudformation validate-template --template-body file://$(TEMPLATE)

package:
	aws cloudformation package --template-file $(TEMPLATE) --s3-bucket $(DEPLOY_BUCKET) --output-template $(PACKAGED) 

deploy: validate package
	aws cloudformation deploy --template-file $(PACKAGED) --stack-name $(STACK_NAME) --capabilities CAPABILITY_IAM

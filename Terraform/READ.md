The first command which we are going to run is -

STEP - 1 - Terraform init # the terraform init command it will download all the provider's dependencies on your local machine.

STEP - 2 : Terraform Plan # As you can see the output of terraform plan, at the end it will show all the resources added and deleted.

STEP - 3 : Terraform apply # You can also see the Tag name - Terraform EC2 which we mentioned in the terraform script.

STEP - 4 : Terraform destroy # It will remove all the running EC2 Instances.


variable.tf and terraform.tfvars -

1. terraform init for PROD

terraform init -var-file="terraform-filename(stage).tfvars"

2. terraform plan for PROD

terraform plan -var-file="terraform-filename(stage).tfvars"

3. terraform apply for PROD

terraform apply -var-file="terraform-filename.tfvars"

4. terraform destroy for PROD

terraform destroy -var-file="terraform-filename.tfvars"

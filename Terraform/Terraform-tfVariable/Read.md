# 1. terraform init for PROD 

terraform init --var-file="terraform-filename(stage).tfvars"

# 2. terraform plan for PROD 

terraform plan --var-file="terraform-filename(stage).tfvars"

# 3. terraform apply for PROD 

terraform apply --var-file="terraform-filename(stage).tfvars"





https://jhooq.com/wp-content/uploads/terraform/terraform-variables/terraform-variable-loading-preference.webp





Terraform.tfvars	                                      variables.tf
It stores variable values	It stores variable definitions such as data type and possible values
Terraform.tfvars are local configuration files	variables.tf files are used to define variables in multiple environments
Terraform.tfvars is sourced automatically by Terraform at runtime	variables.tf must be specified explicitly when running Terraform commands
Variables in Terraform.tfvars are only valid for that particular environment	variables in variables.tf can be used across environments when defined properly
Terraform.tfvars provides default values for the variables declared in variables.tf	variables.tf do not provide any default values 


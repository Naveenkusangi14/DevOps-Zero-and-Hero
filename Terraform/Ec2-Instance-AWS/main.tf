provider "aws" {
  region     = "us-east-"
  access_key = "XXXXXXXXXXXXXXXXXXXX"
  secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
} 
resource "aws_instance" "ec2_user" {
    ami = "ami-0767046d1677be5a0"  
    instance_type = "t2.micro" 
    tags = {
        Name = "Main"
    }
}


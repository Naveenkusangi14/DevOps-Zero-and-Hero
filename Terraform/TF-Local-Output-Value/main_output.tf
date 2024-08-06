



provider "aws" {
   region     = "eu-central-1"
   access_key = <YOUR_ACCESS_KEY>
   secret_key = <YOUR_SECRET_KEY>
}


resource "aws_instance" "example" {
  ami           = "ami-0ff8a91507f77f867"
  instance_type = "t2.micro"
}

# Output-1
output "public_ip" {
  value = aws_instance.example.public_ip
}

#Output-2
output "private_ip" {
  value = aws_instance.example.private_ip
  sensitive = true # it will not print  any sensitive informtion
} 


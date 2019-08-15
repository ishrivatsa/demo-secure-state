# Variables for accepting Access Key and Secret key for AWS
# Default region is set to us-east-1

variable "option_1_aws_access_key" {
}

variable "option_2_aws_secret_key" {
}

variable "region" {
  default = "us-east-1"
}

variable "images" {
  type = map(string)
  default = {
    web  = "ami-07d0cf3af28718ef8"
    mgmt = "ami-0cfee17793b08a293"
    dblb = "ami-07d0cf3af28718ef8"
    db   = "ami-0cfee17793b08a293"
    app  = "ami-07d0cf3af28718ef8"
    api  = "ami-0cfee17793b08a293"
  }
}

variable "option_3_aws_vpc_name" {
}

variable "option_4_aws_vpc_cidr" {
}

variable "option_5_aws_ssh_key_name" {
}

variable "option_6_aws_ssh_key_name" {
}

variable "option_9_use_rds_database" {
}

variable "option_10_aws_rds_identifier" {
}

variable "option_11_multi_az_rds" {
}

variable "product" {
}

variable "team" {
}

variable "owner" {
}

variable "environment" {
}

variable "organization" {
}

variable "costcenter" {
}

    web="ami-0de53d8956e8dcf80"
    mgmt="ami-0a313d6098716f372"
    dblb="ami-0de53d8956e8dcf80"
    db="ami-0a313d6098716f372"
    app="ami-0de53d8956e8dcf80"
    api="ami-0a313d6098716f372"
   }
}


variable "option_3_aws_vpc_name" {}
variable "option_4_aws_vpc_cidr" {}
variable "option_5_aws_ssh_key_name" {}
variable "option_6_aws_ssh_key_name" {}

variable "option_9_use_rds_database" {}
variable "option_10_aws_rds_identifier" {}
variable "option_11_multi_az_rds" {}

variable "product" {}
variable "team" {}
variable "owner" {}
variable "environment" {}
variable "organization" {}
variable "costcenter" {}

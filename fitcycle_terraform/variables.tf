# Variables for accepting Access Key and Secret key for AWS
# Default region is set to us-east-1

#variable "option_1_aws_access_key" {}
#variable "option_2_aws_secret_key" {}
variable "region" {
    default = "us-east-1"
}
variable "images" {
  type = "map"
  default = {
    web="ami-061392db613a6357b"
    mgmt="ami-01e24be29428c15b2"
    dblb="ami-061392db613a6357b"
    db="ami-01e24be29428c15b2"
    app="ami-061392db613a6357b"
    api="ami-01e24be29428c15b2"
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

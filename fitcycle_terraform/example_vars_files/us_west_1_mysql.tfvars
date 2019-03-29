# This file will deploy resources in AWS us-west-1 region
# It will use the MySql EC2 Instance to deploy 
# Set the AWS Access and Secret Key

#option_1_aws_access_key = ""    
#option_2_aws_secret_key = ""
region = "us-west-1"

images = {
    web="ami-029218bb923933d1a"
    mgmt="ami-048ef73aadc6c3bf6"
    dblb="ami-06eb4b1fd6d3fa7f7"
    db="ami-001af27175ceb5c1d"
    app="ami-0cbde20c9254f27cf"
    api="ami-013c6f058d5323ba3"
}

option_3_aws_vpc_name = "fitcycleDemo"
option_4_aws_vpc_cidr = "10.0.0.0/16"


# Add SSH key name here
option_5_aws_ssh_key_name = "adminKey"
option_6_aws_ssh_key_name = "adminKey"

# Deploy MySql EC2 instance.
option_9_use_rds_database = 0
option_10_aws_rds_identifier = 0
option_11_multi_az_rds = 0

product = "fitcycle"
team = "dev-team"
owner = "teamlead"
environment = "staging"
organization = "acmefitness"
costcenter = "acmefitness-eng"

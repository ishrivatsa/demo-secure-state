# This file will deploy resources in AWS us-east-1 region
# It will use RDS instance to deploy 
# Set the AWS Access and Secret Key

#option_1_aws_access_key = ""    
#option_2_aws_secret_key = ""
region = "us-east-1"

option_3_aws_vpc_name = "fitcycleDemo"
option_4_aws_vpc_cidr = "10.0.0.0/16"

# Add SSH key name here
option_5_aws_ssh_key_name = "adminKey"
option_6_aws_ssh_key_name = "devKey"

# Deploy RDS instance.
# Modify option_9 value to 1, to deploy multi-az RDS
# Note : Multi AZ RDS will take atleast 15 min to deploy
option_9_use_rds_database = 1
option_10_aws_rds_identifier = "fitcycleRds"
option_11_multi_az_rds = 0

product = "fitcycle"
team = "dev-team"
owner = "teamlead"
environment = "staging"
organization = "acmefitness"
costcenter = "acmefitness-eng"

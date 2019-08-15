# Provide AWS Access key and Secret Key

provider "aws" {
<<<<<<< HEAD
  access_key = var.option_1_aws_access_key
  secret_key = var.option_2_aws_secret_key
  region     = var.region
=======
  #access_key = "${var.option_1_aws_access_key}"
  #secret_key = "${var.option_2_aws_secret_key}"
  region     = "${var.region}"
>>>>>>> a21e253e26b4007c1e0e785bb70d6e2bdd7f2b95
}

# This allows terraform to backup the *.tfstate file to AWS s3 bucket. Uncomment or Remove the lines to disable remote backup and use local state (Not Recommended)
# terraform {
#   backend "s3" {
#     bucket = "mybucket"
#     key    = "path/to/my/key/some.tfstate"
#     region = "us-east-1"
#   }
# }
# Here it is initialized with empty parameters. Other params can be passed at "terraform init --backend-config="bucket=mybucket" --backend-config="key=path/to/my/key/some.tfstate" --backend-config="region=us-east-1""

#terraform {
#  backend "s3" {
#  }
#}


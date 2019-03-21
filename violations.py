#!/usr/bin/python

#general imports
import json
import pickle
import os
import sys
import datetime
import string
import subprocess


#Logging initialization
import logging
from logging.config import dictConfig
from logging.handlers import SysLogHandler

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'INFO',
        },
        'another.module': {
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(DEFAULT_LOGGING)


def getTerraformFile():

    f = open('Terraform_Output.json', 'r')
    with open('Terraform_Output.json') as f:
        read_data = f.read()
    f.close()

    terraformOutput=json.loads(read_data)

    return terraformOutput


def getVSSOutput():

    f=open('vss_result_object.txt', 'r')
    with open('vss_result_object.txt') as f:
        read_data = f.read()
    f.close()

    vssOutput=json.loads(read_data)

    return vssOutput


def runVSSCli():

    try:
        os.system('vss result object > vss_result_object.txt')
        logging.info("Ran vss cli command")
    except Exception as e:
        print('Exception is %s',e)
        logging.error("Error running vss cli commant %s", e)


def findAndCompare():

    terraformOutput=getTerraformFile()
    vssOutput=getVSSOutput()
    found=False

    igw_id = terraformOutput['igw_id']
    totalViolations=vssOutput['totalItems']

    for item in vssOutput['violations']:
	#print(item['id'])
        if item['id']==igw_id['value'] and item['rule_report']['display_name']=="Publicly routable instance shares ssh-key with administrative instances": #replace vpc with the igw_id and the display name
            logging.info("violation found, %s", item)
            found=True

    return found


if __name__ == '__main__':

# turn on the runVSSCli line to run the Cli command first
#    runVSSCli()
    logging.info("entering main")
    found=findAndCompare()
  #  print("Result of the search is", found)
    print(found)

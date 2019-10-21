import json
import requests
import os
import logging

access_token = ''

refresh_token = os.environ['REFRESH_TOKEN']

## Get Access Token from CSP
def auth():
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    url = 'https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize'
    payload = {"refresh_token": refresh_token }

    response = requests.post(url, data=payload , headers=headers)
    
    if response.status_code == 200:
            print("Success")
            logging.info("Successfully received access token") 
    else:
	 	    logging.error("Failed Retrieving auth token" + str(response.status_code))
    
    data = json.loads(response.content)


    global access_token 
    access_token = data["access_token"]
#    print (access_token)

## Get all the findings within the account 
def all_findings():

    global access_token

    headers = {
        'Content-Type' : 'application/json', 
        'Authorization': 'Bearer {}'.format(access_token)
    }
    payload = "{\n}"
    url = 'https://api.securestate.vmware.com/v2/findings/query'
    response = requests.post(url , data=payload, headers=headers)

    print (response.content)

    # Fetch the continuation Token
    data = json.loads(response.content)
    continuationToken = data["continuationToken"]

    # Get the entire payload for 1000 objects
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(access_token)
    }

# replace cloud provider key with "AWS" for Amazon web services related violations
    payload = "{\n\t\"filters\": {\n\t\t\"cloudProvider\": \"AWS\"\n\t}\n, \n\t\"paginationInfo\":{\n\t\t\"continuationToken\": \"" +  continuationToken + "\",\n\t\t\"pageSize\":1000\n\t}\n}"

    url = 'https://api.securestate.vmware.com/v1/findings/query'
    allFindings = requests.post(url , data=payload, headers=headers)

    print (allFindings)

    return allFindings

## Read Terraform output file
def get_terraform_file():

    f = open('Terraform_Output.json', 'r')
    with open('Terraform_Output.json') as f:
        read_data = f.read()
    f.close()

    terraformOutput=json.loads(read_data)

    return terraformOutput

## Get all violations related to an ObjectID
def get_violation_by_object(all_findings, objectID):
    violations = []
    
    data = json.loads(all_findings.content)
    
    print (objectID)
    ##print (data)
## replace ruleId = "5c8c26847a550e1fb6560cab" for Azure and ruleId = "5c8c26417a550e1fb6560c3f" for AWS for port 22 open
## Tim using ruleId = "5c8c267b7a550e1fb6560c9a" for Virtual Machine Disks not Encrypted in Azure 
    for violation in data["results"]:
        if (violation["objectId"] == objectID and violation["status"] == "Open" and violation["ruleId"] == "5c8c25ec7a550e1fb6560bbe"):
        #if (violation["objectId"] == objectID):
            violations.append(violation)

    if(len(violations) > 0):
	##print ("Violation Found !!")
        return True
    else:
        return False

	 	 
## Main Function
if __name__ == '__main__':
    ## Auth
    auth()
    ## Get all Findings
    resp = all_findings()

    violation_found = []
    terraformOutput=get_terraform_file()
    objectId = terraformOutput['sg_id']
    
    print (objectId)
    
    has_violation = get_violation_by_object(resp, objectId['value'])
    violation_found.append(has_violation)
 
    print("Checking if violations exist \n")
    print(violation_found)
    count = 0 
    for violation in violation_found:
        if (violation == True):
            count +=1
            break
        else:
            continue
    if (count == 0):
	    logging.info("No Violations Found !!")

import json
import requests
import os

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
    data = json.loads(response.content)

    global access_token 
    access_token = data["access_token"]
    print (access_token)

## Get all the findings within the account 
def all_findings():

    headers = {
        'Content-Type' : 'application/json', 
        'Authorization': 'Bearer {}'.format(access_token)
    }
    payload = "{\n\t\"paginationInfo\":{\n\t\t\"continuationToken\": \"\",\n\t\t\"pageSize\": 1000\n\t}\n}"
    ##payload = "{\n}"
    url = 'https://api.securestate.vmware.com/v1/findings/query'
    response = requests.post(url , data=payload, headers=headers)

    return response

## Get all violations related to an ObjectID
def get_violation_by_object(all_findings, objectID):
    violations = []
    
    data = json.loads(all_findings.content)

    #print(data)

    for violation in data["results"]:
        #if (violation["objectId"] == objectID and violation["level"] == "High"):
        if (violation["objectId"] == objectID):
            violations.append(violation)

    print(violations)

    if(len(violations) > 0):
        return True
    else:
        return False

## Main Function
if __name__ == '__main__':
    ## Auth
    auth()
    ## Get all Findings
    resp = all_findings()

    ## Get violations based on object IDs
    objects = ["sg-05d582da5bcbcda6b", "demorsdiag557"]

    for objectId in objects:
        found_violation = get_violation_by_object(resp, objectId)
        print(found_violation)

import requests
import json
import logging

logging.basicConfig(filename="rules.log", format='%(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger('rules')

login_url = "https://10.71.152.30:8443/www/core-service/rest/LoginService/login?alt=json&password=Novell@123&login=admin"

headers={"Content-Type": "application/json; charset=utf-8"}
request = requests.post(login_url, headers, verify=False)
print(str(request))
token = request.json().get('log.loginResponse').get('log.return')

auth_headers ={
    "Authorization": "Bearer "+ token
    }

"""
get_all_rule_ids_url = "https://10.71.152.30:8443/detect-api/rest/v1/rules/allIds"
all_rule_ids_json_response = requests.get(get_all_rule_ids_url, headers=auth_headers, verify=False)

#print(all_rule_ids_json_response.json())
all_rule_ids_list = list(all_rule_ids_json_response)
total_rule_count = len(all_rule_ids_json_response.json())
print("Total No of Rules in ESM: " ,total_rule_count)

for i in range(0, total_rule_count):
    rules_url = "https://10.71.152.30:8443/detect-api/rest/rules/"+all_rule_ids_json_response.json()[i]
    request = requests.get(rules_url, headers=auth_headers, verify=False)
    logger.debug("Rule no: " + str(i))
    logger.debug("Rule Id is: " + all_rule_ids_json_response.json()[i])
    logger.debug("Rule Details: " + str(request.content))
    print(" ")

"""


def get_all_active_list():
    get_all_active_lists = "https://10.71.152.30:8443/detect-api/rest/activelists/allIds"
    all_active_lists_json_response = requests.get(get_all_active_lists, headers=auth_headers, verify=False)

    if("200" in str(all_active_lists_json_response)):
        #print(str(all_active_lists_json_response.content))
        all_active_lists_entries = list(all_active_lists_json_response.json())
        #print(all_active_lists_entries)
        total_active_list_count = len(all_active_lists_entries)
        print("Total No of AL in ESM: " ,total_active_list_count)
        #print(all_active_lists_entries[0])
    else:
        print("!!!!Received error response code : " , all_active_lists_json_response)

    for i in range(0, total_active_list_count):
        al_url = "https://10.71.152.30:8443/detect-api/rest/activelists/ids?ids="+all_active_lists_entries[i]
        request = requests.get(al_url, headers=auth_headers, verify=False)
        logger.debug("AL no: " + str(i))
        logger.debug("AL ID is: " + all_active_lists_entries[i])
        logger.debug("AL Details: " + str(request.content))
        print(" ")
    return all_active_lists_entries


listID = "HXze8iIMBABCAwZh0RxECSA=="

def get_active_list_entry(listID):
    al_entry_url = "https://10.71.152.30:8443/detect-api/rest/activelists/"+listID+"/entries"
    response = requests.get(al_entry_url, headers=auth_headers, verify=False)
    if("200" in str(response)):
        print(response.json())
    
        al_json_dict = json.loads(response.content)
        print("*************", type(al_json_dict))
        for key in al_json_dict:
            print(key, " : ", al_json_dict[key])
            print("\n\n\n")
    
    else:
        print("Error in JSON response" + str(response.content))


def get_active_list_details(listID):
    al_entry_url = "https://10.71.152.30:8443/detect-api/rest/v1/activelists/"+listID
    response = requests.get(al_entry_url, headers=auth_headers, verify=False)
    if("200" in str(response)):
        #print(response.json())
    
        al_json_dict = json.loads(response.content)
        #print("*************", type(al_json_dict))
        """
        for key in al_json_dict:
            print(key, " : ", al_json_dict[key])
            print("\n")
        """
        print(al_json_dict["displayName"])
    else:
        print("Error in JSON response" + str(response.content))



def get_all_esm_rule_list():
    get_all_esm_rule_lists = "https://10.71.152.30:8443/detect-api/rest/rules/allIds"
    all_esm_rule_lists_json_response = requests.get(get_all_esm_rule_lists, headers=auth_headers, verify=False)

    if("200" in str(all_esm_rule_lists_json_response)):
        #print(str(all_esm_rule_lists_json_response.content))
        all_esm_rule_lists_entries = list(all_esm_rule_lists_json_response.json())
        #print(all_esm_rule_lists_entries)
        total_esm_rule_list_count = len(all_esm_rule_lists_entries)
        print("Total No of AL in ESM: " ,total_esm_rule_list_count)
        print(all_esm_rule_lists_entries[0])
    else:
        print("!!!!Received error response code : " , all_esm_rule_lists_json_response)

    for i in range(0, total_esm_rule_list_count):
            get_esm_rule_url = "https://10.71.152.30:8443/detect-api/rest/v1/rules/"+all_esm_rule_lists_entries[i]
            response = requests.get(get_esm_rule_url, headers=auth_headers, verify=False)
            lc = (json.loads(response.content))
            if("cyDNA" in lc["name"]):
                cydna_rules = []
                cydna_rules.append[all_esm_rule_lists_entries[i]]
                logger.debug("Rule no: " + str(i))
                logger.debug("Rule is: " + all_esm_rule_lists_entries[i])
                logger.debug("Rule Details: " + str(request.content))
                print("\n")
                return cydna_rules


if __name__=="__main__": 
    #get_all_active_list()
    #get_active_list_entry(listID)
    #get_active_list_details(listID)
    get_all_esm_rule_list()

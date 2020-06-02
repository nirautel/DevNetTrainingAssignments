import json
import requests
import base64

#Pulling the Token
def Pull_token():
    URL= 'https://sandboxdnac2.cisco.com/api/system/v1/auth/token'
    data={}
    #EncodedCreds = base64.b64encode(bytes(LoginCreds['Username']+':'+LoginCreds['Password'],"utf8")).decode("ascii")
    headers = {
        'Authorization': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'
    }
    response = requests.request("POST", URL, headers=headers, data=data)
    json_data = json.loads(response.text.encode('utf8'))

    return json_data["Token"]


def Show_Data(token):
    URL= 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
    data={}

    headers = {
        'x-auth-token': token
    }
    response = requests.request("GET", URL, headers=headers, data=data)
    json_data = json.loads(response.text.encode('utf8'))

    # Parsing the data for the required attributes
    for line in json_data['response']:
        print('Item ID :   ', line["id"])
        print('Item TYPE :   ', line["type"])
        print('Item FAMILY :   ', line["family"])
        print('Item SOFTWARE :   ', line["softwareType"])
        print('Item IP :   ', line["managementIpAddress"])
        print('\n')



if __name__ == '__main__':
    token = Pull_token()
    Show_Data(token)


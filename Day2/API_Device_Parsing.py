import json
import requests

#Pulling the Token
def Pull_Token():
    URL= 'https://sandboxdnac2.cisco.com/api/system/v1/auth/token'
    data={}
    headers = {
        'Authorisation': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'
    }
    response = requests.request("POST", URL, headers=headers, data=data)

    data_json = json.loads(response.text.encode('utf8'))
    return data_json["Token"]


def Show_Data(Token):
    URL= 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
    data={}
    headers = {
        'x-auth-token': Token,
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
    Token = Pull_Token()
    Show_Data(Token)


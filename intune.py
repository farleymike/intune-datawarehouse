"""Retrieves collections from Intune service using the Intune
Data Warehouse API. Requires the creation of an AA App Registration
that has read access to the Intune Data Warehouse API.

Usage:

    python intune.py parameters.json

    parameters.json example:

    {
        "resource": "https://api.manage.microsoft.com/",
        "tenant" : "<yourtenant>.onmicrosoft.com",
        "authorityHostUrl" : "https://login.microsoftonline.com",
        "clientId" : "xxxxxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "clientSecret" : "xxxxxxxxxxxxxx",
        "intuneAPIEndpoint": "https://<yourapiendpoint>.manage.microsoft.com/ReportingService/DataWarehouseFEService/"
    }
"""
import json
import logging
import os
import sys
import adal
import requests

api_endpoint = ''
api_url = '{endpoint}{collection}?api-version=v1.0&{filter}'
headers = {
    "Content-type": 'application/json',
    "Authorization": ''
}

def turn_on_logging():
    logging.basicConfig(level=logging.WARN)

def get_collection(collection, filter, headers):
    query = api_url.format(endpoint=api_endpoint,collection=collection,filter=filter)
    response = requests.get(query, headers=headers)
    return json.loads(response.content.decode('utf-8'))

turn_on_logging()

parameters_file = (sys.argv[1] if len(sys.argv) == 2 else
                   os.environ.get('ADAL_SAMPLE_PARAMETERS_FILE')
)

if parameters_file:
    with open(parameters_file, 'r') as f:
        parameters = f.read()
    parameters = json.loads(parameters)
else:
    raise ValueError('Please provide parameter file with account information.')

authority_url = (parameters['authorityHostUrl'] + '/' +
                 parameters['tenant']
)
GRAPH_RESOURCE = '00000002-0000-0000-c000-000000000000'
RESOURCE = parameters.get('resource', GRAPH_RESOURCE)

api_endpoint = parameters['intuneAPIEndpoint']

context = adal.AuthenticationContext(authority_url, validate_authority=parameters['tenant'] != 'adfs',)

token = context.acquire_token_with_client_credentials(
    RESOURCE,
    parameters['clientId'],
    parameters['clientSecret']
)

# print("Here's the access token: ", token['accessToken'])
headers["Authorization"] = 'Bearer ' + token["accessToken"]
# print(headers)

# Get top 2 devices as a example. All collections can be found here:
# https://docs.microsoft.com/en-us/intune/developer/intune-data-warehouse-collections
print(get_collection('devices','$top=2',headers))
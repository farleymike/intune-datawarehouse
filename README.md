Example of calling the Intune Data Warehouse API from Python. Sample code will pull two (2) deivces records.

PYthon ADAL Code to obtain a bearer token taken from here:
https://github.com/AzureAD/azure-activedirectory-library-for-python/blob/dev/sample/client_credentials_sample.py

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
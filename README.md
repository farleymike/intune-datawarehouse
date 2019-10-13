# About #
This repo contains examples of calling the Intune Data Warehouse API from Python. Sample code uses a parameters.json file to hold the credentials. You'll need to create one yourself if you want to try out the code.

Python ADAL code to obtain a bearer token taken from here:
https://github.com/AzureAD/azure-activedirectory-library-for-python/blob/dev/sample/client_credentials_sample.py

| Script | Purpose |
| ------ | ------- |
| intune.py |  Connect and retrieve a list of devices. |

# Usage Example: #

`python intune.py parameters.json`

parameters.json example:

```json
{
    "resource": "https://api.manage.microsoft.com/",
    "tenant" : "<yourtenant>.onmicrosoft.com",
    "authorityHostUrl" : "https://login.microsoftonline.com",
    "clientId" : "xxxxxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "clientSecret" : "xxxxxxxxxxxxxx",
    "intuneAPIEndpoint": "https://<yourapiendpoint>.manage.microsoft.com/ReportingService/DataWarehouseFEService/"
}
```
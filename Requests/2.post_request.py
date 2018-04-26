import requests  # Import requests library to send requests to Thingworx

url = 'http://demo.thingsboard.io:80/api/v1/AZXWfYj6hVnwRHsohluH/telemetry'
# Specify the thingsboard url(api)

headers = {
    'Content-Type': 'application/json'
}

# JSON data to upload on Thingworx
data = {"temperature": "30", "humidity": "16"}

response = requests.post(url, headers=headers, json=data)
print 'Response Code:', response.status_code
# If 200 then data has been uploaded successfully
# --------------------------------------------------------------------------- #

# Posting media
files = {'media': open('requests.logo.png', 'rb')}
dict_data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, files=files, data=dict_data)


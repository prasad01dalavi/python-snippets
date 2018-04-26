import requests  # Import requests library to send requests to Thingworx

url = 'http://52.199.28.120:8080/Thingworx/Things/work_thing/Properties/temp'
# temp is one of my property name
value = 12    # Upload 12 on Thingworx

headers = {
    'Content-Type': 'application/json',
    'appkey': '516a7ace-8c01-4744-8640-08226e3fcc3a',
    'Accept': 'application/json',
    'x-thingworx-session': 'true',
    'Cache-Control': 'no-cache',
}

data = {"temp": value}   # JSON data to upload on Thingworx

response = requests.put(url, headers=headers, json=data)
# Note that we have to send put request

print 'Response Code:', response.status_code
# If 200 then data has been uploaded successfully
print 'Response Content:', response.content
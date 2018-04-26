import requests  # supports a fully restful API

url = 'http://google.com'
params = {"search:": "Living Mind Technologies"}
# Parameters passed should be a dictionary
response = requests.get(url, params=params)
print 'Response url:', response.url
# http://www.google.com/?search%3A=Living+Mind+Technologies
"""
The URL for a GET request generally carries some parameters with it.
For requests library, parameters can be defined as a dictionary.
These parameters are later parsed down and added to the base url
or the api-endpoint.
"""
print response.text
print
# print response.json()
# In this case the we will not get json data because google server does not
# return the response in json for this particular url
"""
Now, in order to retrieve the data from the response object,
we need to convert the raw response content into a JSON type data structure.
This is achieved by using json() method. Finally, we extract the required
information by parsing down the JSON type object
"""
# --------------------------------------------------------------------------- #

# Another GET requests example:
r = requests.get('https://api.github.com/events')
print 'Status Code:', r.status_code  # 200
print r.json()  # builtin JSON decoder, in case you're dealing with JSON data
# [{u'payload': {u'size': 1, u'head':....

print 'All Headers:', r.headers
# {'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': ...

print 'Content-type in Header:', r.headers['content-type']
# application/json; charset=utf-8

print 'Binary Response:', r.content
# [{"id":"7588981508","type":"PushEvent" ...
# --------------------------------------------------------------------------- #

# Another GET requests example:
r = requests.get('https://api.github.com/user', auth=('username', 'password'))
print 'Status Code:', r.status_code  # 200
# 4XX client error or 5XX server error response

print 'Headers:', r.headers['content-type']  # application/json; charset=utf-8
print 'All Headers:', r.headers
print 'Encoding:', r.encoding  # utf-8
print 'Response:', r.text
print 'Binary Response:', r.content
print

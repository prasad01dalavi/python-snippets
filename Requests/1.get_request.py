import requests  # supports a fully restful API

url = 'http://google.com'
params = {"search:": "Living Mind Technologies"}
# Parameters passed should be a dictionary
response = requests.get(url, params=params)
print response.url  #
# http://www.google.com/?search%3A=Living+Mind+Technologies
"""
The URL for a GET request generally carries some parameters with it.
For requests library, parameters can be defined as a dictionary.
These parameters are later parsed down and added to the base url
or the api-endpoint.
"""
print response.text

# print response.json()
# In this case the we will not get json data because google server does not
# return the response in json for this particular url
"""
Now, in order to retrieve the data from the response object,
we need to convert the raw response content into a JSON type data structure.
This is achieved by using json() method. Finally, we extract the required
information by parsing down the JSON type object
"""

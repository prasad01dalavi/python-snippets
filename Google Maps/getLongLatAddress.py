import requests   # Import requests module
 
# Google API for geocode
URL = "http://maps.googleapis.com/maps/api/geocode/json"
 
# Specify the name of the location to get the Longitude-Latitudes
location = "Living Mind Technologies"
PARAMS = {'address': location}
response = requests.get(url=URL, params=PARAMS)
# Sending GET request to Google API
 
# Extracting data in json format
data = response.json()

# Extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

print "Latitude:%s\nLongitude:%s\nFormatted Address:%s" % (latitude,
                                                           longitude,
                                                           formatted_address)


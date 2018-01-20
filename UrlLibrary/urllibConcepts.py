#This code should be run in Python 3.x

import urllib.request
x = urllib.request.urlopen('https://www.google.com')
print (x.read())  #Prints the source contents of google.com

url = 'http://pythonprogramming.net'
values = {'s':'basic','submit':'search'} #Providing the searched variable values

data = urllib.parse.urlencode(values)
data=data.encode('utf-8')               #specifying the data encoding format 
req = urllib.request.Request(url,data ) #request for posting
resp = urllib.request.urlopen(req)      #taking the response of posting a request
respData = resp.read()                  #reading the response
print (respData)
            

##
##try:
##    x = urllib.request.urlopen('http://www.google.com/search?q=test')
##    print ("In try block")
##    print (x.read())    #google will not allow to read the content of the website
##    
##except Exception as e:
##    print ("In exception")  #so it will throw an exception
##    print (str(e))           
##
##try:
##    url = 'http://www.google.com/search?q=test'
##    headers = {} #Info about me i.e. browser,operating system, python modules
##    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'  #It's like a browser
##    req = urllib.request.Request(url,headers=headers)
##    resp = urllib.request.urlopen(req)
##    respData = resp.read()
##
##    saveFile = open('withHeaders.txt','w')
##    saveFile.write(str(respData))
##    saveFile.close()
##
##except Exception as e:
##    print (str(e))

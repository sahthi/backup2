import urllib2
response=urllib2.urlopen("http://w3schools.com/xml/cd_catalog.xml")
print response.info()
html=response.read()
response.close()

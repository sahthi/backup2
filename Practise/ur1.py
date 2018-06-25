import urllib2
import xml.etree.ElementTree as ET

url="https://www.w3schools.com/xml/cd_catalog.xml"
data = urllib2.urlopen(url)

with open("cd_catalog.xml","wb+") as f:
      for line in data:
             f.write(line)

tree=ET.parse('cd_catalog.xml')
root=tree.getroot()

for child in root:
    if child.find('COUNTRY').text == 'USA':
        print (child.find("TITLE").text)

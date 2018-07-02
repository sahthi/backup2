'''import requests
import xml.etree.ElementTree as ET

r = requests.get('http://www.w3schools.com/xml/cd_catalog.xml')
tree = ET.parse(r.text)'''
import requests
import xml.etree.ElementTree as ET

r = requests.get('http://www.w3schools.com/xml/cd_catalog.xml',  auth=('user', 'pass'))
tree = ET.parse(r.text)
root = tree.getroot()

with open('data.xml', 'w') as f:
    f.write(r.text)







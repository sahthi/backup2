import xml.etree.ElementTree as ET

tree=ET.parse('items.xml')

root=tree.getroot()
print('Expertise data: ')

for elem in root:
	for subelem in elem:
		print(subelem.text)
	#print(elem)


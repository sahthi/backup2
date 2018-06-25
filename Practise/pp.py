import xml.etree.ElementTree as ET

def createXML(filename):
     root = xml.Element("users")
     children1 = xml.Element("user")
     root.append(children1)
     
     userId1 = xml.subElement(children1,"id")
     userId1.text = "123"
     
     userName1 = xml.subElement(children1,"name")
     userName1.text = "shubam"
     
     tree=xml.ElementTree(root)
     with open(filename,"wb") as fh:
            tree.write(fh)

if __name__ == "__main__":
    createXML("test.xml")








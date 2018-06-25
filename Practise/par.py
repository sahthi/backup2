import xml.dom.minidom
def main():
    doc=xml.dom.minidom.parse("cd_catalog.xml")
    print(doc.nodename)
    print(doc.firstchild.Tagname)

if __name__ == "__main__":
   main()


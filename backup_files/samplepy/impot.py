import re
def findMonthandDate(string):
    regex= r"([a-zA-Z]+)(\d+)"
    match=re.match(regex,string)
    if match==None:
	print("not a valid statement")
        return
 
    print"month:%s",%(match.group(1))
findmonthanddate("jun 24")
print(" ")
findmonthanddate("i was born on jun 24")
   

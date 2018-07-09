import re 
pattern="this is my first python program"
matchobj=re.match(r'this',pattern,re.M|re.I)
if matchobj:
     print "matched",matchobj.group()
else:
     print "no match"

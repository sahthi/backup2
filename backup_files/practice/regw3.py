import re
def match(string):
   text=re.compile(r'^5')
   if text.match(string):
       return True
   else:
       return False
print match('5-236278')
    

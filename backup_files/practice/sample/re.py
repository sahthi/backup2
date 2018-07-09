import re
f=open("file.txt","r")

def text_match(f):
      	pattern="()"
        if re.search(pattern,text):
              return "found a match"
        else:
              return "match not found"
print text_match()



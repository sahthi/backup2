f = open("sample.txt", "rb")
s = f.readlines()
print s
f.close()
f = open("newtext.txt", "wb")
s.reverse()
print s
for item in s:
  print>>f, item
f.close()
          

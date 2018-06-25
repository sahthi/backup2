f=open("sample.txt","rb")
s=f.readlines()
print f
f.close()
f=open("sample.txt","wb")
s.reverse()
for item in s:
    prin item
f.close()

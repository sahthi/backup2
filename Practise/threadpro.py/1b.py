f=open("sample.txt","r+")
s=f.readlines()
print s
f.close()
f=open("new.txt","w+")
f=s.reverse()
print f
for line in s:
    print >> f,line
f.close()

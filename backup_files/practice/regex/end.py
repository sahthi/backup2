f0=open("file1.txt","a+")
inp=input("enter the text:")
while inp!="end":
    f0.write(inp)
    inp=input("enter the text:")
else:
    f0.close()
    f1=open("file1.txt","r")
    f1=f1.read()
    print f1
f0.close()



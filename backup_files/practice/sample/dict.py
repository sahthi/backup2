'''d={'a':1,'b':2,'c':3}
key=raw_input("enter the key to be checked:")
if key in d:
     print "key exist"
else:
     print "key doesn't exist"'''
n=input("enter number:")
d={}
for i in range(1,n+1):
   d[i]=i*i
print d

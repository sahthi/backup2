'''#!/usr/bin/python
l1=[2,13,5,7,6,9]
for x in l1:
    for e in l1:
       if(x+e==15):
          print l1.index(x),l1.index(e)
          l1[l1.index(x)]=l1[l1.index(e)]=0'''
values=[]
for i in range(1000,3000):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
           values.append(s)
print "," .join(values)

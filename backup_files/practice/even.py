l=[]
for i in range(2000,3000):
   if (i%4==0) and (i%5!=0):
       l.append(str(i))
print','.join(l)   


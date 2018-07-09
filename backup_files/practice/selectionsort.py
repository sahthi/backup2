l=[10,9,12,13,7]
size=len(l)
for i in range(0,size):
     for j in range(i+1,size):
         if(l[j]<l[i]):
               min=l[j]
               l[j]=l[i]
               l[i]=min
print l
                

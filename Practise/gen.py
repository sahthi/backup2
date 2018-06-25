def Number(n):
    for i in range(1,n+1):
        if (i%5==0 and i%7==0):
                yield i

n=input("enter number:")
values=[]
for i in Number(n):
       values.append(str(i))
print ",".join(values)

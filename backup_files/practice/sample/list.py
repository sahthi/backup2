i'''#!/usr/bin/python
x=list(input("enter the elements:"))
y=input("enter the number to be multiplied:")
def fun(x,y):
    for i in range(len(x):
         x[i]=x[i]*y
    return x
print fun(x,y)

x = [i*y for i in x]

print x'''

'''def fun(*args):
     sum=0
     for i in args:
          sum=sum+i
     return sum
print fun(1,2,3)'''
import math
x=input("enter no of zeroes:")
i=1
while True:
     res=math.factorial(i)
     if (str(res))[-x:]==[x**0]:
            res[-x:]
            print res,x
            break
     i+=1            

   




#!/usr/bin/python
import math
i=1
x=input("enter number:")
while True:
        res=math.factorial(i)
        if(str(res)[-x:])==(x*"0"):
                print res,i
                break
        i+=1


#!/usr/bin/python
def fun(nu,num):
     for i in range(nu,num):
          if i%7==0:
              yield i
nu=input("enter the first number:")
num=input("enter the second number:")
c=fun(nu,num)
for i in c:
     print i


#!/usr/bin/python
def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact1(n-1)
def fact2(n):
    if n == 0:
        return 1
    else:
        return fact1(n-1) * n 

n=input("enter number:")
print "factorial of ", n,"is :", fact1(n)
n=[3,5,4]

if len(n)>2:
    fact_list=map(fact1,n)
    print fact_list

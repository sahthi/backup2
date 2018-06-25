#!/usr/bin/python
def sum_xorofelem(l1):
        res=0
        length=len(l1)
        for i in range(length):
                for j in range(i+1,length):
                        res+=(l1[i]^l1[j])
        return res

l1=[7,3,5]
l2=[5,9,7,6]
res=sum_xorofelem(l1)
print "The sum of xor of all pairs of numbers in array is:",res
res=sum_xorofelem(l2)
print "The sum of xor of all pairs of numbers in array is:",res

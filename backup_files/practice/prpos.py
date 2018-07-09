#!/usr/bin/python
pos=input("enter which position number u want:")
num=2
count=0
while count!=pos:
      for val in range(2,num):
           if num%val==0:
                num+=1
                break
      else:
                num+=1
                count+=1
print("prime number is position {} is {}." .format(pos,num-1))


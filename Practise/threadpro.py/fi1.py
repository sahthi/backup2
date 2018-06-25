#!/usr/bin/python
l=[]
l1=[]
with open("file1.txt","r+") as f1:
      f2=f1.read().split()
      for i in f2:
          l.append(i)
with open("file2.txt","r+") as f3:
      f4=f3.read().split()
      for j in f4:
          l1.append(j)

for v in l:
      for v1 in l1:
          if (v==v1):
               break
      else:
          print v
      

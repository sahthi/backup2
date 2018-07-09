#!/usr/bin/python
fname=raw_input("enter file name;")
l=raw_input("enter letter to be searched:")
k=0
with open(fname,'r') as f:
    for line in f:
         words=line.split()
         for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("occurences of the letter:")
print(k)



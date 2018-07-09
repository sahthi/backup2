'''#!/usr/bin/python
f=raw_input("enter the file name:")
num_words=0
with open(f,"r") as f1:
      for line in f1:
           words=line.split()
           num_words+=len(words)
print num_words'''
f=raw_input("enter the file name:")
num_lines=0
with open(f,"r") as f1:
     for line in f1:
          num_lines+=1
print num_lines





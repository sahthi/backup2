'''#!/usr/bin/python
f0=raw_input("enter file name:")
num_words=0
with open(f0,'r') as f:
    for line in f:
       words=line.split()
       num_words+=len(words)
print ("number of words:")
print (num_words)'''
fname=raw_input("enter file name:")
fname=list(open(fname))
for line in reversed(fname):
      print (line)

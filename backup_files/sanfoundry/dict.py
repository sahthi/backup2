#!/usr/bin/python
d={'a':1,'b':2,'c':3}
key=raw_input("enter the key to check:")
if key in d.keys():
    print (d[key])
else:
    print key is not present

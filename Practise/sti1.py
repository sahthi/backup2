#!/usr/bin/python
def toggle(mystr):
    l=[]
    for i in mystr:
        if i.upper() != i:
            i=i.upper()
            l.append(i)
        else:
            i=i.lower()
            l.append(i)
    return ''.join(map(str,l))
output=toggle(raw_input())
print output
           
             


     


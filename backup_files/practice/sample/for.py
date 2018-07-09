'''for i in range(6):
    if(i==3 or i==6):
         continue
    print i'''
x=raw_input("enter the string:")
d=0
n=0
for c in x:
    if c.isdigit():
         d+=1
    elif c.isalpha():
         n+=1
    else:
         pass
print "digits ",d
print "characters ",n

        

    



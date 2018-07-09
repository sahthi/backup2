s=raw_input("enter sentence:")
d={Digits:0,Letters:0}
for c in s:
    if c.isdigit():
        d[Digits]+=1
    elif c.isalpha():
       d[Letters]+=1
    else:
        pass
print"Digits:",d[Digits]
print "Letters: ",d[Letters]

        


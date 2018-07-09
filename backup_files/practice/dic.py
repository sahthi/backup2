d={'abc':11,'bc':12,'ca':13}
print("initial dictionary")
print d
key=raw_input("enter the key to delete[a-c]:")
if key in d:
    print d,key,
    del d[key]
    print key
else:
   print "key not found"
 
print "updated dictionary:"
print d

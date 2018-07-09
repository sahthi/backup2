f=open("files.txt","r+")
s=f.read(11)
print "read string is:",s
position=f.tell()
print"position is",position
position=f.seek(2,0)
s=f.read(10)
print "read string is",s



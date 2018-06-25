try:
     f=open("test","r")
     f.write("this is my test file for exception handling")
except IOError:
     print "error:can't find the file or read data"
else:
     print "write operation is performed successfully"
     f.close() 

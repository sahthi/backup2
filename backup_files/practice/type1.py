try:
   fh = open("somefile.txt","w")
   fh.write("this is myn test file for exception handling")
except IOError:
   print("error:can't find the file")
  
    
    

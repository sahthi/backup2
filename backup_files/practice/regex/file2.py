'''x=raw_input("enter string:")
with open("fi.txt","a") as f:
      f.write("\n")
      f.write(x)
with open("fi.txt","r") as f1:
      line=f1.readline()
      while(line!=""):
           print line
           line=f1.readline()'''
with open("fi.txt") as f:
     with open("file.txt","w+") as f1:
             for line in f:
                  f1.write(line)




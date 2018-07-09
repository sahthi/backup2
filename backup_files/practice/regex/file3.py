with open("fi.txt","r") as f:
     for line in f:
         for i in line:
             if(i.isdigit()):
                   print i


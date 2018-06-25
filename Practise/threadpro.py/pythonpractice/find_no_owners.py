import pwd 
import os
uniq=set()

for i in pwd.getpwall():
      	uniq.add(i.pw_uid)

print uniq

home_path=os.getcwd()
for p,sd,fs in os.walk(home_path):
      for i in fs:
         j=p+'/'+i
         if os.path.islink(j):
               print "{0} is a symbolic link and skipping....".format(j)
               continue
         v=os.stat(j)
         print v
         if v.st_uid not in uniq:
             print "the file",j,"has no owner"
     
     
          



import hashlib,os

def get_hash(filename):
     hasher=hashlib.md5()
     with open(filename,"r") as f:
           buf =f.read()
           #print buf
           hasher.update(buf)
           #print hasher
     return hasher.hexdigest()

hashmap = {}

for d,sf,fs in os.walk("./new"):
      for filename in fs:
        
         abs_path = d+'/'+filename
         #print abs_path 
         #if os.path.islink(abs_path) or os.stat(abs_path).st_size<1024:
         if os.path.islink(abs_path):
               continue
         md5_val=get_hash(abs_path)
        
         if md5_val in hashmap:
               matching=hashmap[md5_val]
               print hashmap
               os.unlink(abs_path)
               os.symlink(matching,abs_path)
         else:
               hashmap[md5_val]=abs_path
     


 

import re
name_occ={}
with open("notes.txt","r") as f:
     for line in f:
        mat=re.search("name:([a-z]+)",line)
        if mat:
            name=mat.group(1)
        mat1 =re.search("occupation:([a-z ]+)",line)
        if mat1:
            occupation=mat1.group(1)
            name_occ[name]=occupation
print name_occ

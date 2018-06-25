import re
phrase="21ac63/91ft25"

pat=[r'\d+']
pat1=[r'\D+']

for i in pat:
   mat=re.findall(i,phrase)
   print mat

for j in pat1:
	if j.isalpha(): 
  		mat1=re.findall(j,phrase) 
   		print mat1   

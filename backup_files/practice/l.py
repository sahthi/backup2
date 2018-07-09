num_lines=0
f= open("/home/siddasah/file.txt","r")
data=f.readlines()
print data
for i in data:
	if i == '\n':
		continue
	num_lines+=1

print "number of lines",num_lines   
      

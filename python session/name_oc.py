	import re
nflag = 0
name_occ = {}
with open("notes.txt", "r") as f:
	for line in f:
		mat = re.search("Name:\s+([a-z]+)", line)
		if mat:
			name = mat.group(1)
			nflag = 1
		if nflag == 1:
			mat = re.search("occupation:\s+([a-z ]+)", line)
			if mat:
				occupation = mat.group(1)
				name_occ[name] = occupation
				nflag = 0
			
print "name occ dictionary is:", name_occ					


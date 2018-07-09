wr=open("file1.txt","a+")
while True:
	inp=raw_input()
	if inp=="end":
		break
	else:
		wr.write(inp)
data=wr.read()
print data


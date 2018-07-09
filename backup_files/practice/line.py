l=["one","two","three","four"]
f=open("outfile.txt","w")
for line in l:
    f.write(line)
    f.write("\n")
f.close()

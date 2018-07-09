'''fname=raw_input("enter file name:")
with open(fname,'r') as f:
    for line in f:
        words=line.split()
        for i in words:
             for letter in i:
                 if(letter.isdigit()):
                       print letter'''
f1=raw_input("enter the file to be read from:")
f2=raw_input("enter the file to be appended:")
fin=open(f1,'r')
data=fin.read()
fin.close()
fout=open(f2,'a')
fout.write(data)
fout.close()


             

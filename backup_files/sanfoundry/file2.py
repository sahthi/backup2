'''with open("sample.txt") as f:
     with open("out.txt","w") as f1:
           for line in f:
               f1.write(line)'''
'''fname=raw_input("enter file name:")
with open(fname,'r') as f:
    for line in f:
        words=line.split()
        for i in words:
             for letter in i:
                  if(letter.isdigit()):
                       print letter'''

fname=raw_input("enter file name:")
with open(fname,'r') as f:
     for line in f:
         l=line.title()
         print(l)      

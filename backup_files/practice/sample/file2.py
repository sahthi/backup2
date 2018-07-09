'''
with open("sample1.txt") as f:
     with open("sample.txt","w") as f1:
           for line in f:
               f1.write(line)'''
'''f1=raw_input("enter filename:")
word=raw_input("enter the word to be searched:")
k=0
with open(f1,"r") as f:
     for line in f:
          words=line.split()
     for i in words:
           if (i==word):
                k+=1
print k'''
f1=raw_input("enter file name:")
with open(f1,'r') as f:
    for line in f:
       l=line.title()
       print(l)          
         
    

     




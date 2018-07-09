'''s=raw_input("enter string:")
for i,v in enumerate(s):
     if(i%2==0):
         print v'''
'''s=raw_input("enter sentence:")
word=raw_input("enter word:")
k=0
a=[]
a=s.split(" ")
for i in a:
    if(i==word):
          k+=1
print k'''
s=raw_input("enter comma seperated words:")
word=s.split(" ")
for i in word:
    lis=" " .join(sorted(word))
print lis

    

 
         


    


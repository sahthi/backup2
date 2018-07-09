#!/usr/bin/python
l=[]
def prime_list(start=1,stop=10):
     for i in range(start,stop):
          x=i//2
          for j in range(2,x+1):
               if(i%j==0):
                     break
                     l.append(i)
          return l
print prime_list()
           
     
    

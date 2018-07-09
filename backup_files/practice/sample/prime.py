import sys
def my_list(start=1,stop=100):
     l1=[]
     for num in range(start,stop):
          x=num/2
          for i in range(2,x):
               if num%i==0:
                    break
               else:
                    l1.append(num)
     return l1
val=(sys.argv[1:])
if len(val)<2:
     print my_list()
else:
     start=int(val[0])
     end=int(val[1])
     print my_list(start,stop)  


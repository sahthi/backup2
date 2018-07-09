x=input("enter the number:")
a=1
b=1
l=[]
for i in range(2,x):
      if x%i==0:
           print("number {} is not fibonacci-prime".format(x))
           break
else:
      while a<=x:
           l.append(a)
           a,b=b,a+b
      if x in l:
           print ("number{} is fibonacci-prime".format(x))
      



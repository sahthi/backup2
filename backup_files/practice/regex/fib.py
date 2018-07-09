def fib(num):
    a=1
    b=1
    l1=[]
    for i in range(num):
        l1.append(a)
        a,b=b,a+b
    return l1
print fib(5)
def fib2(num):
   a=1
   b=1
   l1=[]
   while(num>0):
      l1.append(a)
      a,b=b,a+b
      num-=1
   return l1
print fib2(10)
def fib3(num):
   a=0
   b=1
   l1=[]
   for i in range(num):
      l1.append(a)
      a,b=b,a+b
   t=tuple(l1)
   return l1
print fib3(10)
print l1


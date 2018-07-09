import threading
def sum(x,y):
     sum=x+y
     return sum
def sub(x,y):
     sub=x-y
     return sub
x=input("enter number:")
y=input("enter number:")
t=threading.Thread(target=sum)
w=threading.Thread(target=sub)
t.start()
w.start()
      

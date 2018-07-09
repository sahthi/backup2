'''def my_list(li):
    li.append(1)
x=[0]
my_list(x)
x'''
x=list(input("enter:"))
y=input("enter element to multiply:")

def multiply(x,y):
       for i,e in enumerate(x):
           x[i]=e*y
       return x

print multiply(x,y)

           

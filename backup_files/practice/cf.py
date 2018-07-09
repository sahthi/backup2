keys=[]
values=[]
n =int(input("enter number of elements for dictionary:"))
print("for keys:")
for x in range(0,n):
   element=int(input("enter element:"))
   keys.append(element)
print("for values:")
for x in range(0,n):
   element=int(input("enter element:"))
   values.append(element)
d=dict(zip(keys,values))
print("the dictionary is:")
print(d)





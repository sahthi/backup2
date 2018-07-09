keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element:"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element :"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)

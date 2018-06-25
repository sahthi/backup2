n=int(input("enter test cases"))

x=[]

y=[]

c=[]

for i in range(0,n):

      a=raw_input("enter the length of x and y")

      k=raw_input("enter x values")

x=k.split(" ")

o=raw_input("enter y values")

y=o.split(" ")

for i in x:

   for j in y:

      aaa=int(i)

      bbb=int(j)

ab=aaa**bbb

ba=bbb**aaa

if ab>ba:

   c.append(ab)

ab=0

ba=0

print(len(c))

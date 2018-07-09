class gen():
     def __init__(self,end,n):
         self.end=end
         self.n=n
     def Numbers(self):
         for i in range(1,self.end):
              if(i%self.n==0):
                   yield i
end=input("enter the range of number:")
n=input("enter the divisible number:")
c=gen(end,n)
result=c.Numbers()
for number in result:
    print number
              
                           

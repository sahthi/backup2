class check():
      def __init__(self):
           self.n=[]
      def add(self,a):
           return self.n.append(a)
      def remove(self,b):
           return self.n.remove(b)
      def dis(self):
           return (self.n)
obj=check()
choice=1
while choice!=0:
      print("0.Exit")
      print("1.add")
      print("2.delete")
      print("3.display")
      choice=input("enter choice:")
      if choice==1:
          n=input("enter number to append:")
          obj.add(n)
          print("list:",obj.dis())
      elif choice==2:
          n=input("enter number to remove:")
          obj.remove(n)
          print("list:",obj.dis())
      elif choice==3:
          print("list:",obj.dis())
      elif choice==0:
          print("exiting")
      else:
          print("Invalid choice")
print()


      


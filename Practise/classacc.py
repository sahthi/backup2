class Account:
      def __init__(self,name,accnum,balance):   
           self.name=name
           self.accnum=accnum           
           self.balance=balance
      def show(self,name,accnum,balance):
           print "name is: {}".format(self.name)
           print "accnum is:{}".format(self.accnum)
           print "balance is:{}".format(self.balance)
      def deposit(self,amount):
           self.balance+=amount
           print amount,"rupees deposited from ur account"
           return self.balance
      def withdraw(self,amount):
           self.balance-=amount
           print amount,"rupees withraw from ur account"
           return self.balance
      def display_balance(self):
           print "current balance of ur account is",self.balance
           return self.balance
           
           
saving_account=Account("sahithi",123,5000)
print saving_account.show("sahithi",123,5000)
print saving_account.deposit(1000)
print saving_account.withdraw(2000)

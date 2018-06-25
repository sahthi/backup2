l=[]
def summation():
     x=input("enter numbers:")
     sum=0
     for i in x:
         sum+= i
     print sum
     l.append(sum)
def average():
     average=sum/x
def show():
     prompt="""
(S)um
(A)verage
(V)iew
(Q)uit
Enter choice= """
     done=False
     while not done:
           choosen=False
           while not choosen:
                try:
                    choice= raw_input(prompt).lower()
                except(EOFError,KeyboardInterrupt):
                    choice='q'
                    print '\n you picked:[%s]' %choice
                if choice not in 'saq':
                    print'Invalid option,try again'
                else:
                    choosen=True
           if choice=='q':
                 done=True
           if choice=='s':
                 summation()
           if choice=='a': 
                 average()

if __name__=='__main__':
      show()
                

     

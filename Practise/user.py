#!/usr/bin/python
db={}

def newuser():
     prompt='login desired:'
     while True:
         name=raw_input(prompt)
         if db.has_key(name):
              prompt='name taken,try another:'
              continue
         else:
              break
     pwd=raw_input('passwd:')
     db[name]=pwd


def olduser():
     name=raw_input('login:')
     pwd=raw_input('passwd:')
     passwd=db.get(name)
     if passwd==pwd:
          print 'welcome back:',name
     else:
          print 'login incorrect'


def showmenu():
      prompt="""
(N)ew user login
(E)xisting user login
(Q)uit
Enter choice: """
      done=False
      while not done:
           choosen=False
           while not choosen:
                try:
                    choice= raw_input(prompt).lower()
                except(EOFError,KeyboardInterrupt):
                    choice='q'
                    print '\n you picked:[%s]' %choice
                if choice not in 'neq':
                    print'Invalid option,try again'
                else:
                    choosen=True
           if choice=='q':
                 done=True
           if choice=='n':
                 newuser()
           if choice=='e': 


                 olduser()
if __name__=='__main__':
      showmenu()
                





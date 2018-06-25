def thru(func):
       def new(*args,**kwargs):
           print "function has been decorated.congratulations"
           return func(*args,**kwargs)
       return new
@thru
def print_args(*args):
     for arg in args:
          print arg
print_args(1,2,3)
          

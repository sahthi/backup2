'''try:
     num=input("enter number:")
     res=100/num
except ValueError:
     print "value is not int type"
except ZeroDivisionError:
     print "Dont use zero"
else:
     print "result is",res'''
try:
     num=int(raw_input("enter number:"))
     res=100/num
except:
     print "something is wrong"
else:
     print "result is",res

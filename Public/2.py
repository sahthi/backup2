def Ab(a,b):
    try:
         c=((a+b)/(a-b))
    except ZeroDivisionError:
         print "a/b result in 0"
    else:
         print c

Ab(2,3)
Ab(3,3)


import math
x=[10,-5,1.2,'apple']
for i in x:
     try:
        fact=math.factorial(i)
     except TypeError:
        print("factorial is not supported for given input:")
     except ValueError:
        print ("factorial only accepts positive integers")
     else:
        print ("factorial of a", x, "is",fact)
     finally:
        print("release any resources in use")
 

import math
try:
    dividend=float(input("please enter the dividend:"))
    divisor=float(input("please enter the divisor:"))
    quotient=dividend/divisor

except ZeroDivisionError:
    print "can't divide by zero"
finally:
    quotient_rounded=math.round(quotient)
    print quotient_rounded



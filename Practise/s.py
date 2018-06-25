#!/usr/bin/python
import string
alpha=string.letters+'_'
num=string.digits
print 'Welcome to the identifier checker v1.0'
print 'Testees must be atleast 3 chars long'
myInput=raw_input("Identifier to test?")
if(len(myInput))>1:
      if myInput[0] not in alpha:
             print '''Invalid:first symbol must be alphabetic'''
      else:
             for i in myInput[1: ]:
                   if i not in alpha+num:
                        print '''Invalid:remaining symbols must be alphanumeric'''
             else:
                   print "okay,it is an identifier"
                   


	

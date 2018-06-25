#!/usr/bin/python
import string
alpha=string.letters+'_'
digit=string.digits
print 'Welcome to identifier checker v1.0'
print 'Testees mustbe atleast 2 chars long'
myInput=raw_input("enter the test Identifier:")
for i in myInput[0: ]:
       if i not in alpha:
            print '''Invalid,first symbol must be alphabetic'''
       else:
            if i in alpha:
                for i in myInput[1: ]:
                      if i not in alpha+digit:
                           print "Invalid:remaining symbols must be alphanumeric"
                           break
                else: 
                      print"okay,it is an identifier"


           
      


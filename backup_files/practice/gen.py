def fruits():
     yield 'mango'
     yield 'apple'
     yield 'banana'
a=fruits()
print next(a)
print next(a)   
   
     

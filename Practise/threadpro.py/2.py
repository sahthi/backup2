l1 = [("Ramu", "Python", 99),("Jahnavi", "Django", 100),("Kavya", "Flask", 67),("Bhaskar", "Pyramid", 87)]

print "Descending based on couse name: "
d=sorted(l1,key=lambda x:x[1])[::-1]
print d

print "ascending based on marks:"
a=sorted(l1,key=lambda x:x[2])
print a







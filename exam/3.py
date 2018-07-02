#!/usr/bin/python

l1 = [("Ramu", "Python", 99),("Jahnavi", "Django", 100),("Kavya", "Flask", 67),("Bhaskar", "Pyramid", 87)]

print "Descending based on course name::"

x = sorted(l1, key=lambda des: des[1])[::-1]
print x

print "Ascending Based on Marks::"
y = sorted(l1, key=lambda x: x[2])
print y


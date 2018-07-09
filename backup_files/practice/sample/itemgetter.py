'''# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])    

# sort the table by age
import operator
a.sort(key=operator.itemgetter(0))    

# print the table
print(a)'''

l = []
while True:
    s = raw_input()
    l.append(tuple(s.split(",")))

print sorted(l)

number = input("Please enter 3 numbers: ")
number = list(number)

a = int(number[0])
b = int(number[1])
c = int(number[2])

new_l = []

if a > b and a > c:
    new_l.append(a)
    if b > c:
        new_l.append(b)
        new_l.append(c)
    else:
        new_l.append(c)
        new_l.append(b)
    print(new_l)

if b > a and b > c:
    new_l.append(b)
    if a > c:
        new_l.append(a)
        new_l.append(c)
    else:
        new_l.append(c)
        new_l.append(a)
    print(new_l)

if c > a and c > b:
    new_l.append(c)
    if a > b:
        new_l.append(a)
    else:
        new_l.append(b)
        new_l.append(a)
    print(new_l)

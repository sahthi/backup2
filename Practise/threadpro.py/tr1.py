largest=None
smallest=None
while True:
    try:
        number=input("enter numbers: ")
        l=list(number)
        if number == 'done':
               break
        largest=max(l)
        smallest=min(l)
    except:
        print("Invalid input")

print largest
print smallest


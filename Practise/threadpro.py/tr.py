count=0
total=0
while True:
     number = input('enter a number:')
     if number == 'done':
            break
     number=float(number)
     count=count+1
     total=total+number
     print number
print ('total:',total)
print ('count:',count)
print('average:',total/count)

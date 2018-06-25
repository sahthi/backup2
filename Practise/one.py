import random
chars='abcdefghijklmnopqrstuvwxyz'
passwd=' '
for c in range(10):
   passwd +=random.choice(chars)
print passwd

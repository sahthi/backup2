f=open('mbox.txt')
for line in f:
    line = line.rstrip()
    if line.startswith('From: '):
           print line

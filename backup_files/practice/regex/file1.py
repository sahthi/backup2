'''count=0
with open ("fi.txt","r") as f1:
    for line in f1:
        word=line.split()
        print len(word)
        count+=len(word)
print count'''
lines=0
with open("fi.txt","r") as f:
       for line in f:
            lines+=1
print lines


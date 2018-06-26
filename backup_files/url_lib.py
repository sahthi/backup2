import urllib2
response = urllib2.urlopen('http://sixty-north.com/c/t.txt')
data = response.read()
counts = dict()
words = data.split()

for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print counts



import urllib2
from collections import Counter
response = urllib2.urlopen('http://sixty-north.com/c/t.txt')
data = response.read()
print Counter(data.split())


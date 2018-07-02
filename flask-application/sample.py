import urllib2
w=urllib2.urlopen('http://sixty-north.com/c/t.txt')
data=w.read()
print data


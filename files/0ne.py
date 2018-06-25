import re
ip = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')

match = ip.search("Your ip address is 192.168.0.1, have fun!")
if match:
 print 'IP address found:',
 print match.group(), # matching substring
 print 'at position',match.span() # indexes of the substring found
else:
 print 'IP address not found'

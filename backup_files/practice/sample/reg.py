import re
pattern = re.compile("(\d{0,1})")

for i, line in enumerate(open('file.txt')):
    for match in re.finditer(pattern, line):
        print 'Found on line %s: %s' % (i+1, match.groups())
'''import re

textfile = open("file.txt", 'r')
matches = []
reg = re.compile("(\d{0,1})?")
for line in textfile:
    matches += reg.findall(line)
textfile.close()'''

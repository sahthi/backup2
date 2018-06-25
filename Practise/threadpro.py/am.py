import re
string = 'X-DSPAM-Confidence:  0.8475'
r=re.findall(r'\d+',string)
print r

import re
s="I used to have 125.258.143.698 is my phone number,but now i changed it to 587.256.235.125,125.254.148.159"
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', s )
print ip

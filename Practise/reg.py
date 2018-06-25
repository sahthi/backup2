import re
s="ip add of john is 125.258.143.698 and lucy is 125.254.123.200,my machine's ip address was 587.256.235.125 but recently it is changed to 125.254.148.159"
r=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s).group()
print r

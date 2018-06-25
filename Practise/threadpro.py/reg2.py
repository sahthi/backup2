import re
str1 = """Ip adress john's machine is 125.258.143.698 and lucy's machine is 583.244.125.789 and my machine ip adress was 125.254.123.200"""
data = re.findall(r"\d{3}.\d{3}.\d{3}.\d{3}",str1)
op = []
for val in data:
	if all((int(x)<256 for x in val.split('.'))): 
		op.append(val)
print op

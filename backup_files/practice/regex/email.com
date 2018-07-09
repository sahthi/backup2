#!/usr/bin/python
import re
email address=raw_input("enter email:")
p=(\w+)@((\w+\.)+(com))
r=re.match(p,email address)
print r.group(1)


#!/usr/bin/python
import re
s2="I used to have 4563-987-1234,is my phone number,but now i changed it to 567-345-2318,589-574-1258,5874-587-254169"
s1=re.findall(r'\D(\d{3}-\d{3}-\d{4})',s2)
print s1

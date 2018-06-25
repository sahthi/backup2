import re
phrase="1234ev+000 Ts:1234"
match = re.findall(r'(\w{2}):(\d{1,4})',phrase)
print match





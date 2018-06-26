import re
msg = """my mobile number is 783-9088-123 ramesh's mobile number is 897-3154-12343 and suresh mobile nubmer is 376-1234-583 and his friend's mobile number is
38794-1823-458766"""

#3 digits-4 digits-3 digits

print re.findall(r"\b\d{3}\-\d{4}\-\d{3}\b", msg)


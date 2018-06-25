from collections import Counter
from itertools import combinations

l1=['deltas','desalt','lorry','lasted','retainers','salted','areospace','slated','staled','resmelts']
var = combinations(l1,2)
ot=[]
for val in var:
        if Counter(val[0])==Counter(val[1]):
                ot.extend(list(val))
print(list(set(ot)))


l1=[2,13,5,7,6,9]
for x in l1:
    for e in l1:
       if(x+e==15):  
          print l1.index(x),l1.index(e)
          l1[l1.index(x)] = l1[l1.index(e)] = 0
   

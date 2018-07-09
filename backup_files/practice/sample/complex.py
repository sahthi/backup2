x=list(input("enter elements:"))
y=list(input("enter elements:"))
z=1
d=[]
for i in x:
   for j in y:
      if( x.index(i) == y.index(j) ) :
            res=complex(i,j)
	    z*=res
	        # z.append(res)
            d.append(str(res))           
      else:
            pass
print "*" .join(d)





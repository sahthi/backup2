	
def pairORSum(arr, n) :
    ans = 0     
 
    for i in range(0, n) :
         
        for j in range(i + 1, n) :

             ans = ans + (arr[i] ^ arr[j])
             
    return ans
     
arr = list(input("enter:"))

n = len(arr)
 
print(pairORSum(arr, n))
 
 
 


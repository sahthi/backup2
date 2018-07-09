s = raw_input("enter string:")
count = 0
vowels = set("aeiou")
for letter in s:
    if  letter in vowels:
	count+=1
print("count of the vowels is:")
print(count)
	

	


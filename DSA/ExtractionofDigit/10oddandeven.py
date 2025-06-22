low = int(input ("Enter the number low = ")) 
high = int(input("Enter high value = ")) 
even = []
odd = []
for i in range(low ,high+1) : 
    if i %2 ==  0:  
        even.append(i) 
    else: 
        odd.append(i) 
print(even) 
print(odd)
str1 = "Abhi2h4k45" 
sum = 0
for i in range(0, len(str1)): 
    if str1[i].isnumeric() : 
       sum = sum+ int(str1[i]) 

print(sum)
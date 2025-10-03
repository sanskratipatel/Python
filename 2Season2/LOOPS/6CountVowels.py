str1 = "Programming"  
count = 0
for i in range(0 , len(str1)) : 
    if str1[i] in 'aeiou': 
        count =count+1 
        print(str1[i]) 

print("All count ",count)
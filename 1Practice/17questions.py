# Find Missing Number in an array 

num1 = [0,1,2,4,5] 
len1 = len(num1) 

sum1 = 0 
real_sum = sum(num1)

for i in range(0 ,len1+1 ): 
    if i not in num1 : 
        print(f"missing ={i} ")

for i in range(0 , len1+1):  
    sum1 = i+sum1 
    
m =sum1-real_sum
print(f"Missing number = {m}")



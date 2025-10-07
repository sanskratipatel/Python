nums = [1,99,101,98,2,5,3,100,1,1] 

max_count = 0 
for i in range(0 , len(nums)) :
    num = nums[i] 
    count = 1 
    while num +1 in nums: 
        count = count +1 
        num = num +1 
    if max_count < count: 
        max_count = count 

print(max_count) 

# Second solution using sorting 

num1 = [1,99,101,98,2,5,3,100,1,1]  
new_set = set(num1) 
print(new_set) 
num2 = list(new_set)

num2.sort() 
print(num2) 

    
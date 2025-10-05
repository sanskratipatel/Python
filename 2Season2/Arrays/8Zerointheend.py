nums = [1,0,2,4,8,0,7,4,0,6] 

result = [] 

for i in range(0 , len(nums)) : 
    if nums[i] != 0 : 
        result.append(nums[i]) 
       
print(nums) 
print(result) 


for i in range(len(result) , len(nums)) : 
    result.append(0)

print(result) 

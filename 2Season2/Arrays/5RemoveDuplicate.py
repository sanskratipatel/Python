nums = [1,2,4,2,3,4,2,2] 
my_result = [] 

for i in range(0 , len(nums)) : 
    if nums[i] not in my_result: 
        my_result.append(nums[i]) 
print(my_result)
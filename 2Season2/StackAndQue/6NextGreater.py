nums = [1,4,43,5,4,32,6,3,54,7,564,3,423,5,7,8] 

result = [-1] * len(nums) 
# Next greater element  only one  side

for i in range(0 , len(nums)) : 
    for j in range(i+1 , len(nums)) : 
        if nums[j] > nums[i] : 
            result[i] = nums[j] 
            break 

print(result)
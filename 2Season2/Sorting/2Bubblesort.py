nums = [1,2,3,4,52,3,12,53,12] 

for i in range(0 , len(nums)): 
    for j in range(0 , len(nums)-1) : 
        if nums[i] > nums[j] : 
            nums[i],nums[j] = nums[j],nums[i] 

print(nums)
nums = [2,10,12,1,11] 
num2 = nums 
nums.extend(num2)
result =[-1] * (len(nums) //2) 

# Next greater element both side not only one  

for i in range(0 , (len(nums)//2)) :
    for j in range(i+1, len(nums)) : 
        if nums[j] > nums[i] :
            result[i] = nums[j] 
            break 

print(result)

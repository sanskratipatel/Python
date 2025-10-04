nums = [12,32,34,2131,43,21,2] 

largest = nums[0] 

for i in range(0 , len(nums)) : 
    if nums[i] > largest : 
        largest = nums[i] 

print(largest)
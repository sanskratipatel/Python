nums = [5,10,-3,-1,-10,6] 
result = [0] * len(nums) 
pos_index = 0 
neg_index =1
for i in range(0 , len(nums)) : 
    if nums[i] > 0 : 
        result [pos_index] = nums[i] 
        pos_index = pos_index +2
    else: 
        result[neg_index] = nums[i]
        neg_index = neg_index +2 
print(result)

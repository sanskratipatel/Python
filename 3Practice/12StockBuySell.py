nums = [7,5,3,1,4,8,2] 

max_profit = 0
mini = float("inf")
for i in range(0 , len(nums)): 
    if mini > nums[i]: 
        mini = nums[i] 
    if mini> max_profit: 
        max_profit = mini 
print(max_profit)
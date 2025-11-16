nums = [4,1,1,1,0,2,3,5,1] 
maxi = 0  
curr_sum = 0
target = 5
i = 0
for j in range(0 , len(nums)): 
    curr_sum = curr_sum + nums[j] 
    while(curr_sum > target) : 
        curr_sum = curr_sum - nums[i]  
        i = i+1
    if curr_sum == target :
        maxi = max(curr_sum,j-i+1 )
print(maxi)
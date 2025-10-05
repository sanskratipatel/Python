nums = [0,1,2,4,5] 
sum = 0 
real_sum = 0 

for i in range(0 , len(nums)+1) : 
    real_sum = real_sum+i 
    if len(nums) > i:
       sum = sum + nums[i] 
print(sum) 
print(real_sum -sum)
nums = [1,2,3,4,5,6,7] 
n = len(nums) 
num1 = nums[-2:]   
# num1 = num[-3:]
# nums = num[-1]
num2 = nums[0:n-2] 
nums = num1 + num2 

print(nums) 


num4 = [1,2,3,4,5,6,7,8] 
temp = len(num4)   
for i in range(len(num4)-2 ,-1,-1):
    num4[i+1] = num4[i]

num4[0] =temp 

print(num4)
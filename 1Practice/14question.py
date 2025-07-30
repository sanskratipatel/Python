nums = [1,2,3,4,5,0,4,0,5,0]
temp = []
n = len(nums)
for i in range(0 ,len(nums)) : 
    if nums[i] != 0: 
        temp.append(nums[i])  
j = len(temp)
for i in range(0 , len(temp)) : 
    nums[i] = temp[i]


for i in range(j , n) :
    nums[i] = 0

print(nums)
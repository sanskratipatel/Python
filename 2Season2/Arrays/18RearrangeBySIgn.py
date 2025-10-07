nums = [-1,-2,-3,-4,-5,1,2,3,4,5] 

positive = [] 
negative = [] 

for i in range(0 , len(nums)): 
    if nums[i] > 0 : 
        positive.append(nums[i]) 
    else: 
        negative.append(nums[i]) 

for i in range(0 , len(positive)) :  
    nums[2*i] = positive[i] 
    nums[(2*i)+1] = negative[i] 
print(nums)

num2 = [-1,-2,-3,-4,-5,1,2,3,4,5] 
result = [0] * len(num2) 
postindex = 0 
negativeIndex = 1
for i in range(0 ,len(num2)) : 
    if num2[i] >= 0 : 
        result[postindex] = num2[i] 
        postindex = postindex +2 
    else:
        result[negativeIndex] = num2[i] 
        negativeIndex = negativeIndex +2  
print(result)
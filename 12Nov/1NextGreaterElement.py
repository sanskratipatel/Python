nums = [19,4,2,11,6,5,3,10] 
result =[-1] * len(nums)
for i in range(0 , len(nums)-1): 
      for j in range(i+1, len(nums)) : 
            if nums[j] >nums[i] :
                  result[i] = nums[j] 
                  break
print(result) 

# Optimal Solution  
ans = [-1] * len(nums) 

mono_stack =[] 

for i in range(len( nums)-1, -1,-1) :
    while len(mono_stack) != 0 and mono_stack[-1] <= nums[i]:
       mono_stack.pop()
    if len(mono_stack) != 0 :
         ans[i] = mono_stack[-1]
        
    mono_stack.append(nums[i]) 


print(ans)
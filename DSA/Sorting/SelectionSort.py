nums = [1,2,34,534,52,32,134,64,7,4,2,6,7,4] 

# for i in range(0 ,len(nums)) : 
#     min_index = i 
#     for j in range(i+1 , len(nums)): 
#         if nums[j] < nums[min_index] : 
#             min_index = j 
#     nums[i],nums[min_index] = nums[min_index] ,nums[i] 

# print(nums)
            

for i in range(0,len(nums)): 
    max_index = i 
    for j in range(i+1, len(nums)): 
             if nums[max_index] < nums[j]: 
                  max_index = j 
    nums[i] ,nums[max_index] = nums[max_index] ,nums[i]  

print(nums)
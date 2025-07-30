nums = [2,3,4,6,56,67,67,86,4312,343,533,56,78] 


# for i in range(0 , len(nums)):
#     min_index = i 
#     for j in range (i+1,len(nums)): 
#         if nums[j] < nums[min_index]:
#             min_index = j 
#         nums[i] ,nums[min_index] = nums[min_index] ,nums[i] 

# print(nums)

for i in range(0, len(nums)):
    max_index = i 
    for j in range(i+1 , len(nums)):
        if nums[j] > nums[max_index]:
            max_index = j
        nums[max_index], nums[i] = nums[i] ,nums[max_index] 

print(nums)


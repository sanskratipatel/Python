str1 = "aabacbebebe" 
k = 3
my_map = {} 
longest = 0 

i = 0 
for j in range(0 , len(str1)): 
    if str1[j] not in my_map:
        my_map[str1[j]] = 1 
    else : 
        my_map[str1[j]] = my_map[str1[j]]+1
    

    while(len(my_map)> k):
        my_map[str1[i]] =  my_map[str1[i]] -1 
        if  my_map[str1[i]]  == 0 :
            del my_map[str1[i]]
        i = i+1
            
    if len(my_map) == k :
        longest = max(longest, j-i+1)

print(longest)



# for j in range(0 , len(nums)): 
#     curr_sum = curr_sum + nums[j] 
#     while(curr_sum > target) : 
#         curr_sum = curr_sum - nums[i]  
#         i = i+1
#     if curr_sum == target :
#         maxi = max(curr_sum,j-i+1 )
# print(maxi)
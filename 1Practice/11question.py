nums =[1,1,1,1,2,3,2,4,2,3,4,5,3,2,4,3,2] 
my_dict = {} 

for i in range(0 , len(nums)) : 
    if nums[i] not in my_dict: 
        my_dict[nums[i]] = 0
print(my_dict) 

j = 0 
for keys in my_dict: 
    nums[j] = keys
    j = j+1

print("uniques element = ",j) 
print("list = ",nums)


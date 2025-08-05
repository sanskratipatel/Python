nums =[1,23,-3,42,-54,23,-42,13,-44,-23] 
result = [] 
list1 =[]
list2 =[]

for i in range(0 , len(nums)) : 
    if nums[i] > 0: 
        list1.append(nums[i]) 
    else: 
        list2.append(nums[i]) 

for i in range(0 ,len(list1)):
    result.append(list1[i]) 
    result.append(list2[i]) 

print(result) 
result1 =[]  * len(nums)
posindex =0 
negindex = 1
for i in range(0 , len(nums)):
      if nums[i] >=0:
          result1[posindex] = nums[i]
          posindex = posindex+2
      else : 
          result1[negindex] = nums[i]  
          negindex =negindex+2 
print(result1)
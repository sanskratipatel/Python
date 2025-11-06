nums = [1,1,0,1,0,1,1,0,1,1,1] 

maximum = 0 
count = 0

for i in range(0 , len(nums)) : 
    if nums[i] ==1 : 
        count = count +1 
    else: 
        if count >= maximum: 
            maximum = count 
        count = 0 

if count > maximum : 
    maximum = count 
print(maximum)
  
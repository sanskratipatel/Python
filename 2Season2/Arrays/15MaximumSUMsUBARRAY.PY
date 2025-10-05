nums = [-1,3,-2,4,3,-1,3,6,-5,2] 

maxi_sum = float("-inf") 

for i in range(0 ,len(nums)) : 
      total = 0 
      for j in range(i , len(nums)) :  
            total = total + nums[j] 
            if maxi_sum < total : 
                  maxi_sum = total
print(maxi_sum)
            
            
            

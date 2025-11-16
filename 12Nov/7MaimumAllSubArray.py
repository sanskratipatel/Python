nums = [1,3,-1,-3,5,3,6,7]  
key = 3 

i = 0 
j = 0 
result = [] 
res = []


while(j<len(nums)) : 

    if (j-i+1 != key) :
        j = j+1 


for i in range( len(nums)-key+1):
    maxi = 0 
    for j in range(i, i+key):
         if nums[j] > maxi: 
             maxi = nums[j]
    result.append(maxi)
         
print(result)
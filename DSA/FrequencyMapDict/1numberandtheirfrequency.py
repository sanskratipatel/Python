nums = [1,2,3,3,5] 
dict1 = {} 
num2 = int (input("Enter the number thats freqency i want to know  = "))   
for i in range(0 , len(nums)): 
    if nums[i] in dict1: 
        dict1[nums[i]] += 1 
    else: 
        dict1[nums[i]] = 1  

        
print(dict1[num2])
  


print(dict1)
found = False
for key in dict1 : 
    if key == num2 :  
        found = True
        print (dict1[key]) 
if found == False: 
    print("Not exits its accurance is 0")

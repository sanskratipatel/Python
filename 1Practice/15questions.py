nums = [1,2,3,4,5,6,7,8] 
key =5 

found =False

for i in range(0,len(nums)):
    if nums[i] ==key:
        found =True
        print(nums[i]," at ",i,"Place")
        break

if found == False:
    print("Not found")

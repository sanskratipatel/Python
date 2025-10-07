nums = [1,2,4,5,6,7,8,9,10] 
high = len(nums)-1 
low = 0 
key =5 
while(low <= high):
    mid = (low +high)//2 
    if nums[mid] == key : 
        print(key,"is in ",mid, "index")
        break 
    elif nums[mid] > key :  
        high = mid -1 
    else: 
        low = mid +1 

 

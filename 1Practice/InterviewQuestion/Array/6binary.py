num = [1,2,3,4,5,6] 
key =5 
low = 0 
high = len(num) - 1  
found = False
while( low <= high) : 
    mid = (low+high )//2 
    if num[mid] == key : 
       print(mid)
       found = True
       break
    elif num[mid] < key: 
        low = mid+1 
    else : 
        high = mid -1 
   
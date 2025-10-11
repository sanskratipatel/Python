arr = [1, 2 ,0, 4, 3, 0, 5 ,0]
result = [] 
for i in range(0, len(arr)):
    if arr[i] !=0: 
        result.append(arr[i]) 
    
for i in range(len(result) ,len(arr)):
        result.insert(i ,0)

print(result)
    	     
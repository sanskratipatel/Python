# arr = [7, 4, 0, 9, 4, 8, 8 ,2 ,4 ,5 ,5, 1] 
arr = [1 ,5, 3, 4, 3 ,5 ,6]
result = []
answer = float("inf")
temp_answer = -1
found = False
for i in range(0 , len(arr)) : 
    if arr[i] not in result : 
        result.append(arr[i]) 
    else : 
        temp_answer = (arr.index(arr[i]))
       
        found =True
        if temp_answer < answer :  
            answer = temp_answer
        
if found == False : 
   answer = -1
else: 
    answer = answer + 1      

print(answer)
    


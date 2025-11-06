num1 = [1,1,2,3,4,4,5,6,7,7] 
num2 = [1,2,3,5,5,7,7,8,9,12,34] 
result = []
i = 0 
j = 0 

while(j < len(num2) and i < len(num1)) :  
    if num1[i] <= num2[j] : 
        if len(result) ==0 or result[-1] != num1[i]:
            result.append(num1[i]) 
        i = i+1 
    else: 
        if len(result)==0 or result[-1] != num2[j] :
            result.append(num2[j]) 
        j = j +1 


while(i<len(num1) ) : 
    if len(result) == 0 or result[-1] != num1[i] : 
        result.append(num1[i]) 
    i = i+1 

while(j < len(num2)) :
    if len(result) == 0 or result[-1] != num2[j]:
        result.append(num2[j]) 
    j =j+1 

print(result)
num1 = [1,10,13,14,15] 
num2 = [1,1,2,3,4,5,6,8] 

result = []
i = 0 
j = 0  
while((len(num1) >i) and (len(num2) >j )): 
    if num1[i] <=num2[j] : 
        if len(result) == 0  or result[-1] != num1[i] :  
            result.append(num1[i] ) 
        i = i+1 
    else : 
        if len(result) == 0  or result[-1] != num2[j] : 
            result.append(num2[j] ) 
        j = j+1 

while(i < len(num1)) : 
    if len(result) == 0 or result[-1] != num1[i] :
        result.append(num1[i])
    i = i+1


while(j <len(num2)) :
    if len(result) == 0  or result[-1] != num2[j] :
        result.append(num2[j]) 
    j = j+1
print(result)
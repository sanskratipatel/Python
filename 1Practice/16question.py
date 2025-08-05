num1 = [1,2,3,4,5,6,7,9] 
num2 = [1,2,3,4,5,6,11,12,13,14,15,64,76,323] 
len1 = len(num1)
len2 = len(num2)
result = [] 

i = 0 
j = 0 
while i<len1 and j < len2: 
    if num1[i] <=num2[j] :
        if  len(result) == 0 or result[-1] != num1[i]: 
            result.append(num1[i] ) 
        i = i+1
    else : 
        if len(result) == 0 or result[-1] != num2[j] : 
            result.append(num2[j])
        j = j+1

while i<len1 : 
    if len(result) == 0 or result[-1] != num1[i]:
        result.append(num1[i])
    i = i+1
while j<len2:
    if len(result) == 0 or result[-1] != num2[j]:
        result.append(num2[j]) 
    j = j+1
print(result)
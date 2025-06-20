num = int (input('Enter the number = '))  
result = [] 
len = (num+1)//2 
print("Length = ",len)
for i in range(2,len) : 
    if num%i == 0 : 
        result.append(i) 

print(result)

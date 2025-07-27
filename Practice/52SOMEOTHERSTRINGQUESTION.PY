mystr1 = "1 w" 
num1 = 0
num2 = 0 
num3  = 0
for i in range(0 , len(mystr1)):
    if mystr1[i].isnumeric() : 
        num1 +=1 
    elif mystr1[i].isalpha(): 
        num2 += 1
    else : 
        num3 +=1 
print(f"num1 = {num1} num2 {num2} num3 {num3}")
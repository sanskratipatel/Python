number = 153 
number1 = number
new = number 

count = 0 

while(number >0) : 
    count =count +1 
    number = number //10  

arm = 0
while(number1 > 0 ) : 
    arm = (arm) + (number1 %10) **count  
    number1 = number1 //10 


print(arm) 
if arm == new : 
    print("Yes it is")
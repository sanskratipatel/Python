num = int(input("Enter the number = "))  
i =0
num2 = num 
sum =0
while(num > i):
    sum = sum +((num%10)**3) 
    num = num//10 

if(sum == num2):
    print("ArmStrong number ",sum) 
else:
    print("Not ",sum)
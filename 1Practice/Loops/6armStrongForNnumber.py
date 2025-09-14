num = int(input("Enter a number =")) 
sum =0  
armnum = num 
count = 0
while(num >0) : 
    num = num //10 
    count=count + 1  
num2 =armnum
print(num2,"is a Armstrong number") 
print("Count of digits is",count) 
sum = 0
while(num2>0): 
    sum = sum +(num2 % 10) **count
    num2 = num2//10

if (armnum == sum) :
    print(armnum,"is an Armstrong number")
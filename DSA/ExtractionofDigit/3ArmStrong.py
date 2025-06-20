num = int(input("Enter the number = ")) 
num1 = num
num2 = num
n = 0  
count = 0 
while num > 0 : 
    num = num //10 
    count = count +1 
print("Length of number is = " ,count)
    
while num1 > 0 :  
    d =(num1 % 10)
    n = n + (d**count)  
    num1 = num1 // 10 
if(n == num2) : 
    print("Yupppp", n , num2)
else:
    print("Nooo = ",n,num2)
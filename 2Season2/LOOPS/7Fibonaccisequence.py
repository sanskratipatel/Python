num = 10 
num1 = 0 
num2 = 1 
fib = 0
for i in range(2, num+1) : 
    fib = num1 +num2 
    num1 = num2 
    num2 = fib 
    
print(num2)
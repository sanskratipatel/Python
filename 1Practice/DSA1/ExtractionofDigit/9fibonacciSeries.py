num = int(input("Enter the number = ")) 

 
if num == 0 :
    print(0) 
elif num == 1:
    print(1)
else:
    fib1 = 0 
    fib2 = 1 
    for i in range(2, num+1) : 
        fib = fib1+fib2 
        fib1 = fib2 
        fib2 = fib  
    print(fib)
     
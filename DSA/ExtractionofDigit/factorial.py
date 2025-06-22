num = int(input("Enter the number = ")) 
fac = 1  
if num > 0:
    for i in range (1,num+1):  
        print(fac)
        fac = i * fac 
else: 
    fac = 1
      
print("Factorial = ",fac)
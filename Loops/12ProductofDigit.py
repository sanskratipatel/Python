num = int(input("Enter the number = ")) 
i = 0 
product = 1 
while(num >i) :
    product = product * (num%10) 
    num =num // 10  
print(product)
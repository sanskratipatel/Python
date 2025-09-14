num = int(input("Enter the number = ")) 
product =1 
i = 0 
while(num>i):
    product = product * (num %10) 
    num =num//10
print("Product of digits of number is",product)
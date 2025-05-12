num = int(input("Enter the number = ")) 
sum =0

product =1 
while(num > 0) : 
    num2 = num%10  
    # print(num2)
    if(num2%2 ==0) :
        sum = sum + (num%10)
    else:
        product = product * (num%10) 
       
    num =num//10 

print("Sum",sum) 
print("Product",product)
num = int(input("enter the number = ")) 
i = 0
sum =0
while (num >0) : 
    sum = sum + (num%10) 
    num = num//10 

print(sum)
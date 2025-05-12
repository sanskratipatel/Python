num = int(input("Enter the number = ")) 
i = 0 
sum = 0 
while(num >i) : 
    sum = sum + ((num%10)**2) 
    print(sum)
    num = num//10 
print(sum)
num = int(input("Enter the number = ")) 
i =0
sum =0
while(i<num):
    sum =(sum) + ((num%10)**3) 
    num = num//10

print(sum)
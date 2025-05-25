# Sum of All numbers Divible by 4  
sum =0
for i in range(20,51):
    if (i % 4 ==0):
        sum = sum +i 
        print(sum)
print("Sum =",sum)
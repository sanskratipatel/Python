num = int(input("Enter the number = ")) 
i = 2
count =0 
result = []
while((num//2) >=i):
    if (num % i == 0):
        count = count+1
        result.append(i)
    i = i+1 
    
result.append(num)

if count < 2 : 
    print("Prime number ")
else: 
    print(result)
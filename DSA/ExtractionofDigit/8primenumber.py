num = int (input("Enter the number = ")) 
count =0
len = (num+1)//2
print(len)
for i in range(2,len ):  
   
    if num % i == 0: 
        print(i)
        count = count+1  

if count == 0 :
    print("Prime") 
else:
    print("Not prime")  

low = int (input("Enter the low range = ")) 
high = int(input("Enter the high range = ")) 

for i in range(low , high+1 ): 
    if i >1 : 
        is_prime = True 
        for j in range(2, (i+1)//2): 
            if i % j==0 :
                is_prime = False 
                break
        if is_prime == True: 
            print("number = ",i ,end = " ")
            

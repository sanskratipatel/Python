n = int(input("Enter the number = ")) 
i = 0
count = 0
while (n>0): 
    i = i*10 
    count = count +1 
    n = n // 10 

print("count of digit " ,count )
  
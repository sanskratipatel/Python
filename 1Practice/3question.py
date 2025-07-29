num = int(input("Enter the number = ")) 
n = num
num1 =num
count = 0
i=0
while (num>0):
    i =num%10
    count = count+1
    num =num//10 
print(count)
total = 0
while ( n >0) :
    total = total+( n%10)**count 
    n = n//10 
print(total)
if num1 == total: 
    print("yayyyyyyyyyy")
else:
    print("Nooooooooooooo")
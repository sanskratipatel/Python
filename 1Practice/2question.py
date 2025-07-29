n = int(input("Enter the number = ")) 
rev = 0 
num = n
while(n>0): 
    rev = (rev *10) + (n%10)
    n =n//10  

print("Reverse = ",rev) 

if rev == num : 
    print("pallindrom yesss")  
else:
    print("Noooo")
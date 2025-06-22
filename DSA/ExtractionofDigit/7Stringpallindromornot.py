str = input("Enter the string = ") 
rev =""  
str1 = str
for i in range(len(str)-1,-1,-1):
    rev = rev+str[i] 

if(str1 == rev): 
    print("Pallindrom ") 
else:
    print("Not pallindrom" , str1 ,rev)
num = [23,34,45,2,4,342,3,3,4,2,2342,2324,234,43444] 

for i in range(len(num)-2, -1,-1) :
    for j in range(0,i+1):
        if num[j] >num[j+1] : 
            num[j] , num[j+1] = num[j+1] , num[j] 

print(num)  
print("Second largest = ", num[len(num)-2])  



# ++++++++++++++++++++++++++++++++++++++++++++++++++
num2 = [1,23,44,5,343,654,43,5,4,654,3,2] 
largest = float("-inf") 
# print(largest)
sec_largest = float("-inf") 

n = len(num2) 

for i in range(0,n) : 
    largest = max(num2[i],largest)

print(largest)  

for i in range(0,n) : 
    if sec_largest < num2[i] and num2[i] < largest: 
        sec_largest = num2[i]

print(sec_largest)


# ++++++++++++++++++++++++++++++++++++++++++ 

num3 = [12,34,5454,3,323,56,45,34,424,45] 
largest1 = float("-inf") 
smallest = float("-inf") 

for i in range(0,len(num3)):
    if largest1 < num3[i]  :
        smallest=largest1
        largest1= num3[i] 

    elif num3[i] > smallest and num3[i] != largest: 
        smallest = num3[i]
print(smallest)
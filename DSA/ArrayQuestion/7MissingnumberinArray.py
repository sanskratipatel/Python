# num = [] 
# n = int(input("Enter the length of list = ")) 

# for i in range(0,n): 
#     j = int(input(f"Enter {i} index value  = ")) 
#     num.append(j)  
num = [1,3,0,4,5,6,7,8,2]
length = len(num)  
print(length)
realsum = 0
my_sum = 0
for i in range (0, len(num)+1): 
    realsum = realsum + i 
    if i <=  (len(num) -1) : 
       my_sum = my_sum + num[i]  
print(my_sum) 
print(realsum)
missing_num = realsum - my_sum 

print("Missing number in my list is = ", missing_num)


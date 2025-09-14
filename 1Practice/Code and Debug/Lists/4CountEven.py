my_list = [1,2,3,4,5,6,7,8,9] 
count = 0 
sum = 0
for i in range(0, len(my_list)):
    if my_list[i]%2 ==0 :
        sum = sum+my_list[i] 
        count = count+1  

print("sum ",sum, end = " " ) 
print("count",count ,end = " ")
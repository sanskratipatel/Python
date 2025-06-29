num = [0,1,2,3,5,6,7] 
n =len(num) 
my_sum =0
total_sum=0
for i in range(0 , n+1):
    total_sum = total_sum + i  
    if i < n:
        my_sum = my_sum + num[i] 


print("Missing number =", total_sum-my_sum)
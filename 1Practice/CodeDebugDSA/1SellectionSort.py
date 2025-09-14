num = [1,3,44,5,23,55,86,6,7,8] 
n = len(num)  

for i in range(0,n):
    min_index = i 
    for j in range(i+1 , n): 
        if num[min_index] > num[j] :
             min_index = j
        num[min_index], num[i] = num[i] ,num[min_index] 

print(num)
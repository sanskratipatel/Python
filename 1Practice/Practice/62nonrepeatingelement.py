num = [1,32,4,54,6] 
n = len(num) 
for i in range(0 ,n):
    min_index = i 
    for j in range(i+1 , n) :
        if num[j] < num[min_index]:
            min_index = j 
    num[i] , num[min_index] = num[min_index] , num[i]  

print(num)
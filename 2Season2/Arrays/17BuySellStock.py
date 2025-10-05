num = [1,2,4,4,5,2,5,2,3,5,2]   

max_profit = 0 

for i in range(0 , len(num)) :  
    for j in range(i+1 , len(num)): 
        if num[j] > num[i] : 
            profit = num[j] - num[i] 
            if max_profit < profit: 
                print(num[j] , num[i])
                max_profit = profit

print(max_profit)
# Best time to buy or sell stock 

price = [7,2,1,6,3,4,7,1,3,1]

maxi = 0
 
for i in range(0 , len(price)):
    for j in range(i+1, len(price)):
         if  price[j] > price[i] : 
              p = price[j] - price[i]  
              if maxi < p: 
                   print(f"{ price[j]}   == { price[j]}")
                   maxi = p
print(maxi)

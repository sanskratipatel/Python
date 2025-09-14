lis1 = [1,2,3,4,5,6,-78,9,0] 
smallest =float("inf")
second_minimun = float("inf")
for i in range(0 , len(lis1)): 
      if lis1[i] <smallest : 
            smallest = lis1[i] 
print(smallest) 
for i in range(0 , len(lis1)) : 
    if lis1[i] <smallest : 
        second_minimun = smallest
        smallest = lis1[i] 
    elif lis1[i] < second_minimun  and lis1[i] != smallest: 
        second_minimun = lis1[i] 
print(smallest) 
print(second_minimun) 

largest = float("-inf") 
secondlaregerst = float("-inf") 

for i in range (0 , len(lis1)) : 
    if lis1[i] > largest: 
        secondlaregerst = largest 
        largest = lis1[i]
    elif lis1[i] > secondlaregerst and lis1[i] != secondlaregerst:
        secondlaregerst = lis1[i]  
print(largest) 
print(secondlaregerst)
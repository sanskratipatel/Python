my_list = [21,34,56,87,5,6534,23,67,95,44,24,5]  

largest = float("-inf") 
secondlargest = float("-inf") 
smallest = float("inf") 
secondsmallest = float("inf") 

for i in range(0 , len(my_list)):
    if my_list[i] > largest :  
        secondlargest = largest
        largest = my_list[i] 
    elif my_list[i] >secondlargest and my_list[i] <largest:
        secondlargest = my_list[i] 
print(largest )
print(secondlargest)
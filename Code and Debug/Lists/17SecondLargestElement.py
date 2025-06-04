my_lst =[12,34,54,6,5,32] 
larget =  float("-inf")
secondlarget =  float("-inf")

for i in range(len(my_lst)-1):
    if my_lst[i] > larget:
        secondlarget = larget
        larget = my_lst[i]
    elif my_lst[i] > secondlarget: 
        secondlarget = my_lst[i] 
print("Second -largest =", secondlarget) 
print("largest = ",larget)
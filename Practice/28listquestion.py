my_list = [1,2,3,4,6,7,6,7,6,5,43,4,3]  
num =5

if num in my_list:
    index = my_list.index(num) 
    print(index) 
else:
    print("Nope")

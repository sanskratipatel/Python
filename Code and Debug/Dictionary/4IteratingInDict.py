my_dict = { 
    "name":"Ani", 
    "age" :23 ,
    "gender":"Male"
} 
for k in my_dict.keys():
    print(k ,":",my_dict[k]) 
     
marks  = { 
    "A" :1,
    "B":2, 
    "C":3
} 
sum = 0 
for i in marks.values(): 
    sum = sum + i

print("Sum =",sum)
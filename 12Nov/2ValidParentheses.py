str1 = "{[(" 

stack = []
for i in range(0 , len(str1)) : 
    if str1[i] in "{[(":
        stack.append(str1[i]) 
    else:
        if len(stack) ==0 :
            print("Invalid") 
            break 
        ch = stack.pop() 
        if ((str1[i] == ")" and ch == "(") or 
           (str1[i] =='}' and ch =="{") or 
           (str1[i] =="]" and ch =="[")) :
            continue 
        else: 
            print("Invalid") 
           

if len(stack) == 0 : 
    print("valid")
else:
    print("Invalid")
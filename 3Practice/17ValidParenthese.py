s = "(())" 
# s = "[[{()}]]" 
# s = "{[[]]}[" 
s1 = "[{("
stack = []
for i in range(0 , len(s)) : 
    if s[i] in s1 : 
        stack.append(s[i]) 
    else: 
        if len(stack) == 0 : 
           print("Invalid") 
           break 
        ch = stack.pop() 
        if ((s[i] ==")" and ch == "(") or 
           (s[i] =="]" and ch == "[") or 
            (s[i] =="}" and ch == "{")):
            continue 
        else: 
            print("Invalid" ) 
            break
if len(stack) == 0:
    print("Invalid")    

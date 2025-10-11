stack = [] 
s = "{[]}{[]()"

for bracket in range(0 , len(s)) :
   
    if s[bracket] == "(" or s[bracket] == "{" or s[bracket] == "[": 
        stack.append(s[bracket]) 
    else: 
        if len(stack) == 0 : 
            print("Invalid !!!!!!!!!!")
            break 
        ch = stack.pop() 
        if ( 
           ( s[bracket] == ")" and ch =="(" )
           or (s[bracket] == "]" and ch == "[") or 
           (s[bracket] == "}" and ch == "{")
        ): 
            continue 
        else:
            print("Invalid!!!!!!!!!!!!")
            break
else:
   
    if len(stack) == 0:
        print("yayyyyyy")
    else:
        print("Invalid !!!!!!!!!!")
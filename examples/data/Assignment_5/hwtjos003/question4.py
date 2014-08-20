import math
global fString

def f(val):
    global fString
    if "**" in fString:
        y = round(eval(fString.replace("x", str(math.fabs(val)))))
    else:
        y = round(eval(fString.replace("x", str(val))))
        
    return y

fString = input("Enter a function f(x):\n")
for i in range(21):
    for j in range(21):
        if 22 - (i+1) - 11 == f((j+1) - 11):
            char = "o"        
        elif (i+1) == 11 and (j+1) == 11:
            char = "+"
        elif (i+1) == 11:
            char = "-"
        elif (j+1) == 11:
            char = "|"
        else :
            char = " "
            
        print(char, end = "")
    print("")
    

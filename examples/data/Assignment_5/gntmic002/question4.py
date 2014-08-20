import math
f = input("Enter a function f(x):\n")
#if "**" in f:
#    f = "(" + f[0:f.index("**")] + ")" + f[f.index("**"):]
p = ""
for k in range(10,-10-1,-1):
    for j in range(-10,10+1):
        s = f
        s = s.replace("x", "("+str(j)+")")
        
        ans = round(eval(s))
        if ans == k:
            p = p + "o"
        elif j==0 and k==0:
            p = p + "+"
        elif j == 0:
            p = p + "|"
        elif k == 0:
            p = p + "-"
        else:
            p = p + " "
    p = p +"\n"
print(p)
            
               
h = eval(input("Enter the height of the triangle: \n"))
i = 0
s = 1
g = h
while i != h:
    x = " "*(g-1)
    y = s*"*"
    print(x + y)
    g= g-1
    s= s+2
    i = i+1
    

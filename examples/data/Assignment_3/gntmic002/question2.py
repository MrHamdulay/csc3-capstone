#assignment 3.2

h = eval(input("Enter the height of the triangle:\n"))
space = h
for k in range(1,h+1):
    ans = ""
    for j in range(1, space):
        ans = ans+" "
    space = space - 1
    for j in range(1,2*k):
        ans = ans + "*"
    print(ans)
    
    
    
h = eval(input("Enter the height of the triangle: \n"))
c= h-1
r=""
for i in range(h):
    r= (" "*c+("*"*(i+1)))
    print(r+("*"*i))
    c=c-1       
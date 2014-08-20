h = eval(input("Enter the height of the triangle:\n"))
s = (h-1)
n = 1
for i in range(h):
    print(" "*s,"*"*n,sep="")
    n+=2
    s-=1
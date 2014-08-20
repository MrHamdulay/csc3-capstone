height = eval(input("Enter the height of the triangle:\n"))
n=1
for i in range(1,height+1,1):
    print(" "*(height-i),"*"*n,sep='')
    n+=2
        
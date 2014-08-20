height=int(eval(input("Enter the height of the triangle:\n")))
x=height-1
for i in range(1,height+1,1):
    print(x*" ",(2*i-1)*"*",sep="")
    i=i-1
    x=x-1
    
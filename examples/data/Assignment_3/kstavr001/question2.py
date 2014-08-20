x= eval(input("Enter the height of the triangle:\n"))
i=1
y=x
while i <= (y+(y-1)):
    gap=" "*(x-1)
    print(gap,"*"*i,sep="")
    x-=1
    i+=2
    
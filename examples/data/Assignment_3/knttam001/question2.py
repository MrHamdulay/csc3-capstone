h = eval(input("Enter the height of the triangle:\n"))
i = 1
while i<=2*h:
    print(((2*h-i)//2)*" ",i*"*",((2*h-i)//2)*" ",sep="")
    i+=2

h=eval(input("Enter the height of the triangle:\n"))
end=(2*h)-1
gap = end//2
i=1
while i<=end:
    print(" "*gap, end="")
    print("*"*i)
    gap-=1
    i+=2
    
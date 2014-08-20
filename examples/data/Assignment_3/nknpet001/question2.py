def triangle():
    s=eval(input("Enter the height of the triangle:\n"))
    t=s
    for i in range(0,s):
        t=t-1
        print(" "*t+(1+2*i)*"*")

triangle()
def a(par1,par2):
    gap = par1 -1
    for i in range(0, par1*2, 2):
        print(" "*gap, end="")
        print(par2*(i+1), end="\n")
        gap-=1

h=eval(input("Enter the height of the triangle:\n"))
a(h,'*')

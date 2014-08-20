def z(var1,var2):
    gap=(var1//2)-1
    for i in range(0,var1,2):
        print(' '*gap,end='')
        print(var2*(i+1))
        gap=gap-1
x = eval(input("Enter the height of the triangle:\n"))
z(x+x,"*")
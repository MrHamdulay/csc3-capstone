def triangle():
    x=eval(input("Enter the height of the triangle:\n"))
    space=x//1
    for i in range(0,x+4,2):
            print(' '*space,end='')
            print("*"*(i+1))
            space-=1
triangle()



def triangle():
    x=eval(input("Enter the height of the triangle:\n"))
    space=x-1
    for i in range(0,x+x,2):
        #space=x-i
        print(' '*(space),end='')
        print("*"*(i+1))
        space=space-1  
triangle()
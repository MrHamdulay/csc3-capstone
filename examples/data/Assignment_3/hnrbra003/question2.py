h=eval(input("Enter the height of the triangle:"))
def triangle():
    for i in range(h+1):
        for j in range(h-i):      # h being 5, i being 0 initially
            print(" ", end='')
        for k in range(i*2-1):
            print("*", end='')
        print()

triangle()
    
    
    
    
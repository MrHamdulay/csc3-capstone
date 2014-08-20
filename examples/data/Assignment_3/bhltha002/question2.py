def triangle():
    H=eval(input("Enter the height of the triangle:\n"))
    gap=H-1
    x=1
    for i in range(H):
        print(gap*' '+x*'*')
        gap-=1
        x+=2
    
triangle()

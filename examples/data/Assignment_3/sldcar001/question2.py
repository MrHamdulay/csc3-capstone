def triangle():
    h=eval(input("Enter the height of the triangle:\n"))-1
    m=1
    while h>=0:
        print(h*" ",m*"*", sep='')
        h-=1
        m+=2
    
    
triangle()
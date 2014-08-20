def iso():
    h = eval(input("Enter the height of the triangle: \n"))
    
    gap = h - 1
    for i in range(1, 2 * h, 2):
        print(" " * gap, "*" * i, sep = "")
        gap-=1
        
iso()
    
    
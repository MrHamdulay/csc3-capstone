def vector():
    import math
    a = input("Enter vector A:\n")
    b = input("Enter vector B:\n")
    total = [a.split(" ")] + [b.split(" ")] 
    
    # Converts strings to numbers so they can be evaluated
    for j in range(3):
        total[0][j] = eval(total[0][j])
        total[1][j] = eval(total[1][j])
    
    # Calculates dot production with vectors
    dot_production= 0
    for i in range(3):
        dot_production += total[0][i] * total[1][i]   
    
    # Calculates normalisation with vectors for A
    A = 0
    for x in range(3):
        A += total[0][x]**2
    A = math.sqrt(A)
    
    
    # Calculates normalisation with vectors for B
    B = 0
    for y in range(3):
        B += total[1][y]**2
    B = math.sqrt(B)    
    
    
    # Calculates addition with vectors 
    add = []
    for k in range(3):
        add += [total[0][k] + total[1][k]]
    
    
    print("A+B =", add)
    print("A.B =", dot_production)
    print("|A| = %.2f" % A)
    print("|B| = %.2f" % B)   
    
vector()
    
































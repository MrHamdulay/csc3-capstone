# Assignment 6 - Question 2
# A program that does basic vector calculations in 3 dimensions (addition, dot product and normalization)
# Written by: Laene van Niekerk 
# VNKLAE001

vector_A = (input("Enter vector A:\n"))
vector_B = (input("Enter vector B:\n"))
A = vector_A.split(" ")
B = vector_B.split(" ")

def addition():     # Function to do addition of vectors
    add_A = []
    for number_A in A:  # Converts string into numbers
        number_A = eval(number_A)
        add_A.append(number_A)
    add_B = []        
    for number_B in B:  # Converts string into numbers
        number_B = eval(number_B)
        add_B.append(number_B)
    addition = []
    pos = 0
    for num in add_A:   # Adding the vectors by looping through A and adding number to corresponding position in B
        ans = num + add_B[pos]
        pos = pos + 1
        addition.append(ans)
    print("A+B =", addition)

def dot_product():      # Function to do multiplication of vectors
    dp_A = []
    for number_A in A:  # Converts string into numbers
        number_A = eval(number_A)
        dp_A.append(number_A)
    dp_B = []        
    for number_B in B:  # Converts string into numbers
        number_B = eval(number_B)
        dp_B.append(number_B)  
    dot_product = []    # Creates the new vector for dot products
    pos = 0
    for num in dp_A:    # Loops through each value in list A and multiplies it with the corresponding value in list B
        ans = num * dp_B[pos]
        pos = pos + 1
        dot_product.append(ans)
    total = 0
    for i in dot_product:
        total = total + i
    print("A.B =", total)
    
def norm_A():
    import math
    norm_A = []
    for number_A in A:      # Converts strings into numbers
        number_A = eval(number_A)
        norm_A.append(number_A)
    squares = []
    for num in norm_A:  # Squares each value in list A and creates a new list with these values
        ans = num*num
        squares.append(ans)
    root = math.sqrt(squares[0] + squares[1] + squares[2])  # Finds the square root of the sum of the numbers in the squares list
    normalization = "{0:.2f}".format(root)   # Rounds the square root to 2 decimal places
    print("|A| =", normalization) 
    
def norm_B():   # Same loop as for norm_A is executed for B to do normalization for list B
    import math
    norm_B = []
    for number_B in B:
        number_B = eval(number_B)
        norm_B.append(number_B)
    squares = []
    for num in norm_B:
        ans = num*num
        squares.append(ans)
    root = math.sqrt(squares[0] + squares[1] + squares[2])
    normalization = "{0:.2f}".format(root)
    print("|B| =", normalization)     
    
addition()
dot_product()
norm_A()
norm_B()
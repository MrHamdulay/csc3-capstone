"""Program to calculate vectors
Tyrone Arnold
24/05/2014"""


def vect_calc():
    import math
    
    A_vector = input("Enter vector A:\n") #gets new vector A
    A_vector_new= A_vector.split(' ') #splits vectors with space
    B_vector = input("Enter vector B:\n") #gets vector B
    B_vector_new=B_vector.split(' ') #splits vector B with space
    
    
    A_int=[int(i) for i in A_vector_new] #
    B_int=[int(i) for i in B_vector_new] #
    
    add_A_B = [(A_int[0]+B_int[0]), (A_int[1]+B_int[1]), (A_int[2]+B_int[2])] #adds ints indexed to the same position
    multiply_A_B= (A_int[0]*B_int[0]+ A_int[1]*B_int[1]+ A_int[2]*B_int[2]) #multiplies ints indexed to the same position
    abs_val_A= (math.sqrt(A_int[0]**2+A_int[1]**2+A_int[2]**2)) #finds the absolute value of A
    abs_val_B= (math.sqrt(B_int[0]**2+B_int[1]**2+B_int[2]**2)) # finds the absolute value of B
    print("A+B =",add_A_B)
    print("A.B =",multiply_A_B)
    
    if A_int!=[0,0,0] and B_int!=[0,0,0]: #checks values in array 
        print("|A| =",round(abs_val_A, 2)) #prints the absolute value of A
        print("|B| =",round(abs_val_B, 2)) #prints the absolute value of B
    
    elif A_int ==[0,0,0] and B_int == [0,0,0]: #checks value in array
        print("|A| = 0.00") #if A and B are = 0
        print("|B| = 0.00")
vect_calc()
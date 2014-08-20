"""Akhil Singh
SNGAKH004
23April 2014"""


#Get vectors from user
vector_A=input("Enter vector A:\n")
vector_B=input("Enter vector B:\n")
#split vectors into a list of 3 and converting them into integers
vector_A=vector_A.split()
vector_B=vector_B.split()
for a in range(3):
        vector_A[a]=eval(vector_A[a])
        vector_B[a]=eval(vector_B[a])

#Addition Calculation
add_vector=[]
for z in range(3):
        add_vector.append(vector_A[z]+vector_B[z])
print("A+B =",add_vector)        
                                       

#Performing the dot calculation
dot = 0
for w in range(3):
        dot+=vector_A[w]*vector_B[w]
print("A.B =",dot)

#Absolute value Calculation        
add_squares_A=0
add_squares_B=0
for s in range(3):
        add_squares_A=add_squares_A+vector_A[s]**2
        add_squares_B=add_squares_B+vector_B[s]**2
print("|A| = {0:0.2f}".format(add_squares_A**(1/2)))
print("|B| = {0:0.2f}".format(add_squares_B**(1/2)))          
        

       
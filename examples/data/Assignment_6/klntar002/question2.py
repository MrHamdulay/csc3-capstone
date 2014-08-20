# tarisai kalinde
# klntar002
# vector mathematics

import math

# input of vector componet values
veca=input('Enter vector A:\n')
vecb=input('Enter vector B:\n')

# assigning of vector values
# int to turn string to value
vector_a=veca.split(' ')
vector_b=vecb.split(' ')

# mathematics of vectors
add_vect=[(int(vector_a[0])+int(vector_b[0])),(int(vector_a[1])+int(vector_b[1])),(int(vector_a[2])+int(vector_b[2]))]     #addition
print('A+B =',add_vect)

multi_vect=[(int(vector_a[0])*int(vector_b[0]))+(int(vector_a[1])*int(vector_b[1]))+(int(vector_a[2])*int(vector_b[2]))]   #multiplication

print('A.B =',multi_vect[0])

modulus_a=math.sqrt((int(vector_a[0])*int(vector_a[0]))+(int(vector_a[1])*int(vector_a[1]))+(int(vector_a[2])*int(vector_a[2]))) #modulus
if modulus_a==0:
    print('|A| = 0.00')
else:    
    print('|A| =',(round(modulus_a,2)))

modulus_b=math.sqrt((int(vector_b[0])*int(vector_b[0]))+(int(vector_b[1])*int(vector_b[1]))+(int(vector_b[2])*int(vector_b[2]))) # modulus
if modulus_b==0:
    print('|B| = 0.00')
else:    
    print('|B| =',(round(modulus_b,2)))






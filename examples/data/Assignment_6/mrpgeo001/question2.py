"""Program for vector calculations
Geoff Murphy
MRPGEO001
20 April 2014"""

from math import sqrt

Vector_A = []
Vector_B = []

Vec_A_input = input("Enter vector A:\n")
Vec_B_input = input("Enter vector B:\n")

Vec_A_List = Vec_A_input.split() #Splits the given numbers into a list
Vec_B_List = Vec_B_input.split()
#-------------------------------------------------------------------------------

for i in Vec_A_List:
    if i != ' ':
        i = eval(i)
        Vector_A.append(i)  #Turns the given vectors into lists of numbers and appends them to a new list variable
    else:
        continue


for j in Vec_B_List:
    if j != ' ':
        j = eval(j)
        Vector_B.append(j)
    else:
        continue
  
#-------------------------------------------------------------------------------

Add = []

Add_x = Vector_A[0] + Vector_B[0] #Adds the corresponding components of the vectors and appends that value to the new list 'Add'
Add.append(Add_x)

Add_y = Vector_A[1] + Vector_B[1]
Add.append(Add_y)

Add_z = Vector_A[2] + Vector_B[2]
Add.append(Add_z)

print("A+B", "=", Add)

#-------------------------------------------------------------------------------

Mult = []

Mult_x = Vector_A[0] * Vector_B[0] #Multiplies the corresponding components of the vectors and appends that value to the new list 'Mult'
Mult.append(Mult_x)

Mult_y = Vector_A[1] * Vector_B[1]
Mult.append(Mult_y)

Mult_z = Vector_A[2] * Vector_B[2]
Mult.append(Mult_z)

Mult = Mult[0]+Mult[1]+Mult[2]  #Then adds all of these multiplied components together
print("A.B", "=", Mult)

#-------------------------------------------------------------------------------

A_norm = (Vector_A[0]*Vector_A[0])+(Vector_A[1]*Vector_A[1])+(Vector_A[2]*Vector_A[2])  #Multiplies all the components by themselves, i.e. squares them, and then adds them together
A_norm = sqrt(A_norm)
print('|A| =', '{0:.2f}'.format(A_norm)) #Formats the answer to two decimal places


B_norm = (Vector_B[0]*Vector_B[0])+(Vector_B[1]*Vector_B[1])+(Vector_B[2]*Vector_B[2])
B_norm = sqrt(B_norm)
print('|B| =', '{0:.2f}'.format(B_norm))


#-------------------------------------------------------------------------------
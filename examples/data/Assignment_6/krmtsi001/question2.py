import math
#are we assuming we have 2 vectors only?



A_vector=input("Enter vector A: \n")
#how do you assure that the user puts a space inbetween

B_vector=input("Enter vector B: \n")



A=A_vector.split()   #making a string into a list
B=B_vector.split()



addpos1=eval(A[0])+eval(B[0])     #changing each list value into a number
addpos2=eval(A[1])+eval(B[1])
addpos3=eval(A[2])+eval(B[2])

addA_B=[addpos1, addpos2, addpos3]     
print("A+B =",addA_B)

dotpos1=eval(A[0])*eval(B[0])
dotpos2=eval(A[1])*eval(B[1])       #changing each list value into a number
dotpos3=eval(A[2])*eval(B[2])

dot_product=(dotpos1+dotpos2+dotpos3)  #calculating dot product
print("A.B =",dot_product)

square_A=eval(A[0])**2+eval(A[1])**2+eval(A[2])**2  #calculating square with format using two decimal places
print("|A| =","%.2f"%(math.sqrt(square_A)))

square_B=eval(B[0])**2+eval(B[1])**2+eval(B[2])**2   #calculating square with format using two decimal places
print("|B| =","%.2f"%(math.sqrt(square_B)))







             
             








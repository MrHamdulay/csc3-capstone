#Rushil Kalidas
#Vector calculation

A= input("Enter vector A:\n")
B= input("Enter vector B:\n")

A= A.split(' ')
B= B.split(' ')

A_B= []
A_B.append(eval(A[0])+eval(B[0]))
A_B.append(eval(A[1])+eval(B[1]))
A_B.append(eval(A[2])+eval(B[2]))

A_times_B= (eval(A[0])*eval(B[0]))+(eval(A[1])*eval(B[1]))+(eval(A[2])*eval(B[2]))

import math

norm_A = "{0:0.2f}".format(math.sqrt(eval(A[0])**2+ eval(A[1])**2 + eval(A[2])**2))
norm_B = "{0:0.2f}".format(math.sqrt(eval(B[0])**2+ eval(B[1])**2 + eval(B[2])**2))

print('A+B =', A_B)
print('A.B =', A_times_B)
print('|A| =', norm_A)
print('|B| =', norm_B)


    
    
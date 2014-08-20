""" program that does basic vector calculations
nelisile mkhwebane
21/04/2014 """

import math

A = []
B = []
""" get the vectors from user"""

vector_A  = input("Enter vector A:\n")
vector_B = input ("Enter vector B:\n")

"""split the entered string into a list """
vector_A = vector_A.split(" ")
vector_B= vector_B.split(" ")

""" add the string to the list """

A.append(vector_A[0])
A.append(vector_A[1])
A.append(vector_A[2])

B.append(vector_B[0])
B.append(vector_B[1])
B.append(vector_B[2])


""" isolating each component """
Ai = A[0]
Aj = A[1]
Ak = A[2]

Bi = B[0]
Bj = B[1]
Bk = B[2]
""" to get the sum of the vectors """
vector_sum = []
sum_i= (eval(Ai)+eval(Bi))
sum_j= (eval(Aj)+eval(Bj))
sum_k= (eval(Ak)+eval(Bk))

#gettting the sums into the list
vector_sum.append(sum_i)
vector_sum.append(sum_j)
vector_sum.append(sum_k)

import math
""" to get the dot product """
dot_pro = eval(Ai)*eval(Bi) + eval(Bj)*eval(Aj) + eval(Ak)*eval(Bk)

""" to get |A| """
magnitude_A = round(math.sqrt((eval(Ai))**2 + (eval(Aj))**2+ (eval(Ak))**2),2)
magnitude_B = round(math.sqrt((eval(Bi))**2 + (eval(Bj))**2+ (eval(Bk))**2),2)

"""getting the output"""

print ("A+B","=", vector_sum)
print ("A.B","=", dot_pro)
if magnitude_A == 0:
    print ("|A|","=", "0.00")    
    
else:
    print ("|A|","=", magnitude_A)
if magnitude_B == 0:
    print("|B|","=", "0.00")
else:
    print ("|B|","=", magnitude_B)

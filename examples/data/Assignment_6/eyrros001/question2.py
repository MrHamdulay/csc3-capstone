"""program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
Ross Eyre
20/05/2014"""

import math

#get vector values and put into list
vectorA = input("Enter vector A:\n")
vectorA = vectorA.split(" ")

vectorB = input("Enter vector B:\n")
vectorB = vectorB.split(" ")

#calculate addition of vectors
def vector_addition():
    ans1 = eval(vectorA[0])+eval(vectorB[0])
    ans2 = eval(vectorA[1])+eval(vectorB[1])
    ans3 = eval(vectorA[2])+eval(vectorB[2])

    newVector = [ans1, ans2, ans3]
    print("A+B =", newVector) 

#calc dot product of vectors
def vector_dot_product():
    ans1 = eval(vectorA[0])*eval(vectorB[0])
    ans2 = eval(vectorA[1])*eval(vectorB[1])
    ans3 = eval(vectorA[2])*eval(vectorB[2])
    
    ans = ans1+ans2+ans3
    print("A.B =", ans)
    
#calculate norm of vector(s)    
def vector_norm():
    #VectorA
    Aans1 = eval(vectorA[0])**2
    Aans2 = eval(vectorA[1])**2
    Aans3 = eval(vectorA[2])**2
    
    Asquare = "{0:0.2f}".format(math.sqrt(Aans1+Aans2+Aans3))
    
    #vectorB
    Bans1 = eval(vectorB[0])**2
    Bans2 = eval(vectorB[1])**2
    Bans3 = eval(vectorB[2])**2
        
    Bsquare = "{0:0.2f}".format(math.sqrt(Bans1+Bans2+Bans3))
    
    print("|A| =", Asquare)
    print("|B| =", Bsquare)
    
    
#call methods    
vector_addition()
vector_dot_product()
vector_norm()


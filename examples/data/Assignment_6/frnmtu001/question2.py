"""This function does basic vector calculation in 3 dimensions : addition, dot product and normalization
Mtunzi France
24 April 2014"""
def vector():
    import math
    #Ask the user to input both vectors then adds them to two lists
    vector_A = input("Enter vector A:\n")
    vector_B = input("Enter vector B:\n")
    A = vector_A.split()
    B = vector_B.split()
    """Converts all the strings in the ist to intergers"""
    A = list(map(int, A))
    B = list(map(int, B))
    """Vector addition"""
    Sums = []
    sum1 = A[0] + B[0]  #adds first items in the two lists
    sum2 = A[1] + B[1]  #adds second items in the two lists
    sum3 = A[2] + B[2]  #adds third items in both lists
    Sums.append(sum1)
    Sums.append(sum2)
    Sums.append(sum3)
    """Vector dot product"""
    product = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]
    """Vector normalization"""
    normA = math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
    normB = math.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
    """Print out all the answers"""
    print("A+B =",Sums)
    print("A.B =",product)
    if normA != 0:
        print("|A| =",round(normA, 2))
    else:
        print("|A| = {0:0.2f}".format(normA))
    if normB != 0:
        print("|B| =",round(normB, 2))
    else:
        print("|B| = {0:0.2f}".format(normB))
vector()
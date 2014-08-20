#VRMNIC005
# asssignment 6 question 2

from math import sqrt

Vector_A = list(map(int, input("Enter vector A: \n").split())) #takes inputs, creates a list of integers
Vector_B = list(map(int, input("Enter vector B: \n").split()))

def Vector_add(a, b):
    """ performs vector addition"""
    result_vector = []
    for i  in range(len(a)):
        final = a[i]+ b[i] #adds corresponding elements
        result_vector.append(final) #appends them to a new list
    return result_vector


def Vector_Dot(a, b):
    """Performs vector dot product"""
    result = 0
    for i in range(len(a)):
        final = a[i] * b[i] #multiplies corresponding elements
        result+= final
    return result


def Vector_Norm(x):
    """Performs vector normalization"""
    final_result = 0
    for i in range(len(x)):
        result = x[i]**2 #squares each element
        final_result += result #adds squared elements
    Norm= round(sqrt(final_result), 2) #square roots and rounds answer to 2 decimal places
    return Norm

print("A+B =", Vector_add(Vector_A, Vector_B))
print("A.B =", Vector_Dot(Vector_A, Vector_B))
print("|A| =", "{:.2f}".format(Vector_Norm(Vector_A)))
print("|B| =", "{:.2f}".format(Vector_Norm(Vector_B)))


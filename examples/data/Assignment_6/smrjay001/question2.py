"""
Assignment 6 - Question 2
Program to perform baisic vector calculation in 3 dimensions
Jayan Smart
April 2014
"""

from math import sqrt

def vec_add(vec_A, vec_B):#Compute Addition:
    x_sum = vec_A[0] + vec_B[0]
    y_sum = vec_A[1] + vec_B[1]
    z_sum = vec_A[2] + vec_B[2]  
    vec_AplusB = [x_sum, y_sum, z_sum]

    print("A+B =", vec_AplusB)

def vec_dot(vec_A, vec_B):#Compute Dot-Product:
    x_dot = vec_A[0] * vec_B[0]
    y_dot = vec_A[1] * vec_B[1]
    z_dot = vec_A[2] * vec_B[2]  
    vec_AdotB = (x_dot + y_dot + z_dot)

    print("A.B =", vec_AdotB)

def norm_A(vec_A): #Compute Norm A:
    norm_A = sqrt((vec_A[0])**2 + (vec_A[1])**2 + (vec_A[2])**2)

    print ("|A| =", "{:.2f}".format(norm_A)) 

def norm_B(vec_B):#Compute Norm B:
    norm_B = sqrt((vec_B[0])**2 + (vec_B[1])**2 + (vec_B[2])**2)

    print ("|B| =", "{:.2f}".format(norm_B))

    
def main():
    #Recieve imput of vectors A and B:
    vec_A = input("Enter vector A:\n")
    vec_A = vec_A.split()
    for i in range(len(vec_A)):
        vec_A[i] = eval(vec_A[i])

    vec_B = input("Enter vector B:\n")
    vec_B = vec_B.split()
    for i in range(len(vec_B)):
        vec_B[i] = eval(vec_B[i])

    vec_add(vec_A, vec_B)       #Compute Addition:
    vec_dot(vec_A, vec_B)       #Compute Dot-Product:
    norm_A(vec_A)               #Compute Norm A:
    norm_B(vec_B)               #Compute Norm B:

main()

#-------------------------------------------------------------------------------
# Name:        Question 2
# Purpose:     Assignment 6
#
# Author:      Taylor
#
# Created:     23/04/2014
# Copyright:   (c) Taylor 2014
#-------------------------------------------------------------------------------
import math

def add():
    """Adds two given vectors"""

    result = [] #create empty list

    #add corresponding components from vector A and B
    x_component = eval(vector_A[0]) + eval(vector_B[0])
    y_component = eval(vector_A[1]) + eval(vector_B[1])
    z_component = eval(vector_A[2]) + eval(vector_B[2])

    #append these components into my list
    result.append(x_component)
    result.append(y_component)
    result.append(z_component)

    print("A+B = {0}".format(result))

def dot():
    """solves the dot product of any two given vectors"""

    #multiplies corresponding components from vector A and B
    x_component = eval(vector_A[0]) * eval(vector_B[0])
    y_component = eval(vector_A[1]) * eval(vector_B[1])
    z_component = eval(vector_A[2]) * eval(vector_B[2])

    #sum up the components
    sumOfproducts = x_component + y_component + z_component

    print("A.B = {0}".format(sumOfproducts))

def norm():
    """Normalises a given vector"""
    #calculate magnitude of A and then vector B
    A = math.sqrt((eval(vector_A[0])**2 + eval(vector_A[1])**2 + eval(vector_A[2])**2))
    B = math.sqrt((eval(vector_B[0])**2 + eval(vector_B[1])**2 + eval(vector_B[2])**2))

    #round magnitudes to 2 decimals places and print them
    print("|A| = {0:.2f}\n|B| = {1:.2f}".format(A, B))



#Main program
#prompt user for vectors and call functions

vector_A = input("Enter vector A:\n").split(" ")
vector_B = input("Enter vector B:\n").split(" ")

add()
dot()
norm()
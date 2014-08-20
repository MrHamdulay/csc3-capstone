"""Basic Vector Calculations program
2014/04/23
Tauhirah Eguardo"""
import math
def str_list(string):
    #use to make input of three digits a list - easier to work with
    array = string.split(" ")
    return array

def addition(A,B):
    #use list addition to add vectors
    C = []
    for i in range(len(A)):
        newvalue = eval(A[i]) + eval(B[i])
        C.append(newvalue)
    return C

def dot_rule(A,B):
    C = []
    for i in range(len(A)):
        newvalue = eval(A[i]) * eval(B[i])
        C.append(newvalue)
    dot = 0
    for i in range(len(C)):
        dot += int(C[i])
    return dot    

def norm(A):
    C = []
    for i in range(len(A)):
        newvalue = eval(A[i]) * eval(A[i])
        C.append(newvalue)
    dot = 0
    for i in range(len(C)):
        dot += int(C[i])
    dot = math.sqrt(dot)
    return dot     
    
def main():
    A = input("Enter vector A:\n")
    B = input("Enter vector B:\n")
    A = str_list(A)
    B = str_list(B)
    print("A+B =",addition(A,B))
    print("A.B =",dot_rule(A,B))
    print("|A| =","%0.2f" % norm(A))
    print("|B| =","%0.2f" % norm(B))
    
main()
    
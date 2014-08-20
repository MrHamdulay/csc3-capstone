# Author : Rayaan Fakier FKRRAY001
# Date : 20 - 04 - 2014
# question2.py
'''Program that performs basic vector calculations in 3 dimensions 
(addition, dot product and normalization)'''

import math

def main():
    veca = input("Enter vector A:\n")
    vecb = input("Enter vector B:\n")
    # Seperates each vector component individually
    veca_list = veca.split()
    vecb_list = vecb.split() 
    
    # Prints and evaluates vector addition
    print("A+B = ["+str(eval(veca_list[0]) + eval(vecb_list[0])) + ", " + str(eval(veca_list[1]) + eval(vecb_list[1])) + ", " + str(eval(veca_list[2]) + eval(vecb_list[2]))+ "]")
    
    # Prints and evaluates vector dot product
    print("A.B =", (eval(veca_list[0]) * eval(vecb_list[0])) + (eval(veca_list[1]) * eval(vecb_list[1])) + (eval(veca_list[2]) * eval(vecb_list[2])))
    
    # Evaluate vector A's and vector B's norm
    veca_norm = math.sqrt((eval(veca_list[0])**2) + (eval(veca_list[1])**2) + (eval(veca_list[2])**2))
    vecb_norm = math.sqrt((eval(vecb_list[0])**2) + (eval(vecb_list[1])**2) + (eval(vecb_list[2])**2))
    if veca_norm == 0:
        print("|A| = 0.00")
    else:
        print("|A| =",round(veca_norm,2))
    if vecb_norm == 0:
        print("|B| = 0.00")
    else:
        print("|B| =",round(vecb_norm,2))
    
main()
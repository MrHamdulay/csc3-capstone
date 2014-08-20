"""Question 2 
20 April 2014
by Jonathan Ovadia"""
import math
def main():
    vector_a = input("Enter vector A:\n").split(" ")
    vector_b = input("Enter vector B:\n").split(" ")
    for i in range(len(vector_a)):
        vector_a[i] = eval(vector_a[i])
    for i in range(len(vector_b)):
        vector_b[i] = eval(vector_b[i])        
    vector_sum = [vector_a[0]+vector_b[0],vector_a[1]+vector_b[1],vector_a[2]+vector_b[2]]
    vector_product = vector_a[0]*vector_b[0] + vector_a[1]*vector_b[1] + vector_a[2]*vector_b[2]
    mod_a = math.sqrt(vector_a[0]**2+vector_a[1]**2+vector_a[2]**2)
    mod_b = math.sqrt(vector_b[0]**2+vector_b[1]**2+vector_b[2]**2)
    print("A+B =",vector_sum)
    print("A.B =",vector_product)
    print("|A| =","{:.2f}".format(mod_a))
    print("|B| =","{:.2f}".format(mod_b))

main()
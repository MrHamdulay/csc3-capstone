"""A6Q2 - 3D Vector Caclculations
CRNKEE002
21/4/2013"""

import math

VectorArray = []

def main():
    vector_get()
    vector_add(VectorArray)
    vector_dot_product(VectorArray)
    vector_norm("A", VectorArray[0])
    vector_norm("B", VectorArray[1])
    
def vector_get():
    global VectorArray
    A = input("Enter vector A:\n")
    B = input("Enter vector B:\n")
    VectorArray.append(A.split(" "))
    VectorArray.append(B.split(" "))


def vector_add(VectorArray):
    newstr = ""
    for i in range(3):
        newstr += str(int(VectorArray[0][i]) + int(VectorArray[1][i]))
        if i != 2:
            newstr += ', '
    print("A+B = [" + newstr + ']')
    
def vector_dot_product(VectorArray):
    product = 0
    for i in range(3):
        product += int(VectorArray[0][i])*int(VectorArray[1][i])
    print("A.B = " + str(product))
    
def vector_norm(name, vector):
    temp = 0
    for i in range(3):
        temp += int(vector[i])**2
    temp = "{0:.2f}".format(math.sqrt(temp))
    print('|', name, '| = ', temp, sep="")
    
if __name__ == "__main__":
    main()
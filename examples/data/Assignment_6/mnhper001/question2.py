#Author:Percival Munhuwaani
#Program: A program to do basic vector calculations in 3 dimensions
#Date:24/04/2014
import math #accessing mathematical functions from the maths module
def main():
    vector1=input("Enter vector A:\n") #getting the first vector
    vector2=input("Enter vector B:\n") #getting the second vector
    list1=vector1.split() #putting the inputs into a list
    list2=vector2.split() #putting the inputs into a list
    x1=list1[0]
    x2=list1[1]
    x3=list1[2]
    y1=list2[0]
    y2=list2[1]
    y3=list2[2]
    sum=[int(x1)+int(y1),int(x2)+int(y2),int(x3)+int(y3)]#addition of the vectors
    product=int(x1)*int(y1)+int(x2)*int(y2)+int(x3)*int(y3)#dot product  of the vector
    vector1_sqrt=(math.sqrt(int(x1)**2+int(x2)**2+int(x3)**2))#normalization of the vector
    vector2_sqrt=(math.sqrt(int(y1)**2+int(y2)**2+int(y3)**2))#normalization of the vector
    print("A+B =",sum)
    print("A.B =",product)
    print("|A| =","%.2f"%(vector1_sqrt))
    print("|B| =","%.2f"%(vector2_sqrt))
    


main()


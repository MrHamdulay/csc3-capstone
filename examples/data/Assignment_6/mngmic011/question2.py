"""question 2
Assignment 6
Micaela Menegaldo"""

import math

def addition_vectors(a,b):
    position1=(int(a[0])+int(b[0]))
    position2=(int(a[1])+int(b[1]))
    position3=(int(a[2])+int(b[2]))
    print("A+B = [",position1,", ",position2,", ",position3,"]",sep='')
    
def dotproduct(a,b):
    position1=(int(a[0])*int(b[0]))
    position2=(int(a[1])*int(b[1]))
    position3=(int(a[2])*int(b[2]))
    result=position1+position2+position3
    print("A.B = ",result,sep='')
    
def norm(a,b):
    resultA=round(math.sqrt((int(a[0]))**2+(int(a[1]))**2+(int(a[2]))**2),2)
    resultA="{0:0<4}".format(resultA)
    print("|A| = ",resultA,sep='')
    resultB=round(math.sqrt((int(b[0]))**2+(int(b[1]))**2+(int(b[2]))**2),2)
    resultB="{0:0<4}".format(resultB)
    print("|B| = ",resultB,sep='')

if __name__=='__main__':
    vector_A_string=input("Enter vector A:\n")
    vector_B_string=input("Enter vector B:\n")
    
    vector_A_list=vector_A_string.split(" ")
    vector_B_list=vector_B_string.split(" ")    
    
    addition_vectors(vector_A_list,vector_B_list)
    dotproduct(vector_A_list,vector_B_list)
    norm(vector_A_list,vector_B_list)
'''program to do basic Vector calculations in 3 dimensions
sankara mallane
21 april 2014'''

V_A = [] #Values in Vector A
V_Astr = (input("Enter vector A:\n"))
V_A = V_Astr.split(' ') 
       
V_B = [] #Values in Vector B
V_Bstr = (input("Enter vector B:\n"))
V_B = V_Bstr.split(' ') 

import math

def add(): #Add the values in Vector A and B together
        list_Add = []
        for i in range(len(V_A)):
                list_Add.append (eval(V_A[i])+eval(V_B[i]))
        print('A+B =',list_Add)

def multiply(): #Multiply the values in Vector A and B together
        list_Multi = []
        for i in range(len(V_A)):
                list_Multi.append (eval(V_A[i])*eval(V_B[i]))
        print('A.B =',list_Multi[0]+list_Multi[1]+list_Multi[2])

def squareroot_A(): #Squareroot the values in Vector A 
        for i in range(len(V_A)):
                V_A.append (eval(V_A[i]))
        print('|A| =',"%0.2f"%round(math.sqrt(eval(V_A[0])**2 + eval(V_A[1])**2 + eval(V_A[2])**2),2))
        
     
def squareroot_B(): #Squareroot the values in Vector B 
        for i in range(len(V_B)):
                V_B.append (eval(V_B[i]))
        print('|B| =',"%0.2f"%(round(math.sqrt(eval(V_B[0])**2 + eval(V_B[1])**2 + eval(V_B[2])**2),2)))
add()
multiply()
squareroot_A()
squareroot_B()

'''
x=(eval(V_A[0])**2 + eval(V_A[1])**2 + eval(V_A[2])**2)
        print ( a"{%.2f}" )
'''
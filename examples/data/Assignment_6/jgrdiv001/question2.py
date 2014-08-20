import math
"""program to do vector functions
Author: Divan Jagers
25 April 2014"""
a = input("Enter vector A:\n") #prompts input from user
vector1 =(a.split())            # creates list for vector 1
for i in range(len(vector1)):
    vector1[i]= eval(vector1[i])    #evaluates every element in list
b = input("Enter vector B:\n")      #prompts input from user
vector2 =(b.split())             # creates list for vector 2
for i in range(len(vector2)):     #evaluates every element in list
    vector2[i]= eval(vector2[i])     
vector_list = []                 # A list that has vector 1 list and vector 2 list
vector_list.append(vector1)
vector_list.append(vector2)       
def addition():          #addition of the two vector lists
    z = []
    for i in range(len(vector_list[0])):
        c = (vector_list[0][i]+vector_list[1][i])
        z.append(c)
    return z
def multiplication():     #multiplication of two lists
    z = []
    for i in range(0,len(vector_list[0]),3):
        a = (vector_list[0][i]*vector_list[1][i]+vector_list[0][i+1]*vector_list[1][i+1] + vector_list[0][i+2]*vector_list[1][i+2])
        #z.append(a)
    return a
def sqrtA():        #finds square root of items in list A(vector1)
    z = []
    for i in range(len(vector1)):
        a = (vector1[i]**2)
        
        z.append(a)
    final = 0    
    for item in z:
        final+=item
    ans="%.2f" % round(math.sqrt(final),2)
    return ans

def sqrtB():         #finds square root of items in list A(vector1)
    z = []
    for i in range(len(vector2)):
        a = (vector2[i]**2)
        
        z.append(a)
    final = 0    
    for item in z:
        final+=item
    ans="%.2f" % round(math.sqrt(final),2)
    return ans
print("A+B =",addition())         #prints all the functions
print("A.B =",multiplication())
print("|A| =",sqrtA())
print("|B| =",sqrtB())

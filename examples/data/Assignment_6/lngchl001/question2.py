#program to do basic vector calculations in 3 dimensions
#by Chloe Longmore
# 23 April 2014

import math

#asks for vector input
vector_A=input("Enter vector A:\n")
vector_B=input("Enter vector B:\n")

#splits input into spearate characters
vector_A=map(int,vector_A.split())
vector_B=map(int,vector_B.split())

#creates lists
vec_a_list=[]
vec_b_list=[]

#adds characters to lists, elminates spaces
for i in vector_A:
    if i==' ':
        continue
    vec_a_list.append(i)

for i in vector_B:
    if i==' ':
        continue
    vec_b_list.append(i)

#convertes items in list into integers    
vec_b_list=[int(i) for i in vec_b_list]   
vec_a_list=[int(i) for i in vec_a_list]

#function that does vector addition
def vector_addition():
    vec_add=[a+b for a,b in zip(vec_b_list, vec_a_list)]
    print("A+B =",vec_add)   

#function that does vector dot product    
def vector_dot_product():
    vec_dot=sum([a*b for a,b in zip(vec_a_list,vec_b_list)])
    print("A.B =",vec_dot)

#function that does vector A normalization    
def vector_a_normalization():
    normal=round(math.sqrt(sum([a**2 for a in vec_a_list])),2)
    normal="%.2f" %normal
    print("|A| =",normal)
#function that does vector B normalization    
def vector_b_normalization():
    normal=round(math.sqrt(sum([b**2 for b in vec_b_list])),2)
    normal="%.2f" %normal
    print("|B| =",normal)
    
    
vector_addition()
vector_dot_product()
vector_a_normalization()
vector_b_normalization()


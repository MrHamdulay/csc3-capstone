"""program to do vector calculations
22 April 2014
herman claassens"""

import math
A=input('Enter vector A:\n') # get both vectors
B=input('Enter vector B:\n')

vector_A=A.split()  # turn vectors into string list
vector_B=B.split()

added_list=[] # add each corresponding item in the lists together
for n in range(len(vector_A)) and range(len(vector_B)):
    added_list.append(eval(vector_A[n])+eval(vector_B[n]))
    
multiplied_list=[] # multiply each corresponding list item
for n in range(len(vector_A)) and range(len(vector_B)):
    multiplied_list.append(eval(vector_A[n])*eval(vector_B[n]))
Total=0
for a in multiplied_list: # add the multiplied numbers together
    Total+=a
    
def norm(lists):
    number_list=[] # turn the string list into a integer list
    for a in lists:
        x=eval(a)
        number_list.append(x)
    squared=0
    for a in number_list:   # square each number in the list
        squared_number=a**2
        squared+=squared_number# get the total value of all the squared numbers in the list
    return squared
    
    
A_squared=norm(vector_A) 
B_squared=norm(vector_B)

root_A=math.sqrt(A_squared) # get square root of the total squared value
root_B=math.sqrt(B_squared)

print('A+B =',added_list)  # print answers of calculations
print('A.B =',Total)
print('|A| = {0:<.2f}'.format(root_A))
print('|B| = {0:<.2f}'.format(root_B))
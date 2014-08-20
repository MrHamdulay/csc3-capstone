#22 April 2014
#Tayla Radmore
#Vectors

import math
# Getting vector A
a=input("Enter vector A: \n")   
a_list=a.split(' ')

#Getting vector B
b=input("Enter vector B: \n")   
b_list=b.split(' ')

#creating the adding part
new_list=[]
for i in range(3):
    new_number=eval(a_list[i])+eval(b_list[i])
    new_list.append(new_number)
    
print("A+B =",new_list)

#creating the timesing part
new_list=[]
for i in range(3):
    new_number=eval(a_list[i])*eval(b_list[i])
    new_list.append(new_number)
    total = 0
    for x in new_list:
        total+=x
    
print("A.B =",total)

# absolute of a
if a=="0 0 0": print("|A| = 0.00")
else:
    total=0
    for i in a_list:
        i = eval(i)
        total+=i*i
    square_root=math.sqrt(total)

    print("|A| =", round(square_root,2))
    

# absolute of b
if b =="0 0 0":print("|B| = 0.00")
else:
    total=0
    for i in b_list:
        i = eval(i)
        total+=i*i
    square_root=math.sqrt(total)
    
    print("|B| =", round(square_root,2))
    

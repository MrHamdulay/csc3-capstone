"""program to do basic vector calculations
Jacqueline Blomendahl
23/04/2014"""

import math
#getting input and creating empty lists
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")
Alist=(A.split())
Blist=(B.split())
newlist= []
new_list= []
Newlist= []
New_list=[]
#finding A+B
for i in range(3):
    newlist.append(eval(Alist[i])+eval(Blist[i]))
    
print("A+B = ", newlist, sep='')

#finding A.B
for i in range(3):
    new_list.append(eval(Alist[i])*eval(Blist[i]))
add_product= new_list[0]+new_list[1]+new_list[2]    
print("A.B = ", add_product, sep='')

#finding |A|
for i in range(3):
    Newlist.append(eval(Alist[i])**2)
addproduct= Newlist[0]+Newlist[1]+Newlist[2]
if addproduct==0.0:
    print("|A| = ", "0.00", sep='')
else:
    print("|A| = ", round(math.sqrt(addproduct), 2), sep='')

#finding |B|
for i in range(3):
    New_list.append(eval(Blist[i])**2)
Addproduct= New_list[0]+New_list[1]+New_list[2]
if Addproduct==0.0:
    print("|B| = ", "0.00", sep='')
else:
    print("|B| = ", round(math.sqrt(Addproduct), 2), sep='')
    
        
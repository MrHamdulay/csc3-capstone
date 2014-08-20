

import math
x=input("Enter vector A:\n")
qwe=x.split(" ")
y=input("Enter vector B:\n")
rty=y.split(" ")
list1=[]
list2=[]
list3=[]
list4=[] #create 4 empty lists
for i in range(len(qwe)): #length qwe = length rty
    a=(eval(qwe[i])+eval(rty[i])) 
    b=(eval(qwe[i])*eval(rty[i]))
    c=(eval(qwe[i])**2)
    d=(eval(rty[i])**2)
    list1.append(a)
    list2.append(b)
    list3.append(c)
    list4.append(d) #add respective variables to respective empty lists
product=0
squarea=0
squareb=0 #assign zero values to variables to be used later
print("A+B =",list1)
for j in range(len(list2)):
    product=list2[j]+product
    squarea=list3[j]+squarea
    squareb=list4[j]+squareb
print("A.B =",product)
if qwe==['0', '0', '0']:
    print("|A| = 0.00")
else:
    print("|A| =", round(math.sqrt(squarea),2))
if rty ==['0', '0', '0']:
    print("|B| = 0.00")
else:
    print("|B| =", round(math.sqrt(squareb),2)) #print what is necessary

    

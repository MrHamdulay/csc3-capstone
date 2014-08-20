#maisha ivha
#24/04/2015
#a program to do basic vector calculations in 3 dimensions: addition, dot product and normalization

import math
def main():
    list1=[]
    list2=[]
    w=input("Enter vector A:\n").split()
    q=input("Enter vector B:\n").split()
    #evaluating and appending the inputs to the list
    list1.append(eval(w[0]))
    list1.append(eval(w[1]))
    list1.append(eval(w[2]))
    list2.append(eval(q[0]))
    list2.append(eval(q[1]))
    list2.append(eval(q[2]))

   
   #THE FORMULAS THAT CAN BE USED TO CALCULATE THE OUTPUTS ASSIGNED 
    e=[list1[0]+list2[0],list1[1]+list2[1],list1[2]+list2[2]]
    t=list1[0]*list2[0]+list1[1]*list2[1]+list1[2]*list2[2]
    o=math.sqrt(list1[0]**2+list1[1]**2+list1[2]**2)
    p=math.sqrt(list2[0]**2+list2[1]**2+list2[2]**2)
    #THE output to be  printed out
         
    print("A+B =",e)
    print("A.B =",t)
    #control function incase the input is 0
    if o==0 and p==0:
        print("|A| = 0.00")
        print("|B| = 0.00")
    else:
        print("|A| =",round(o,2))
        print("|B| =",round(p,2))        
main()
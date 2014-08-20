'''
Prashanth Sridharan
SRDPRA001
Assignment 3
Question 02
'''
ht = eval(input("Enter the height of the triangle:\n"))

i=1
j=1
spc=" "*(ht-1)
spc_ht = ht-1
while(i<=ht):
    print(spc,"*"*j,sep="")
    i=i+1
    spc_ht=spc_ht - 1
    spc=" "*spc_ht
    j=j+2

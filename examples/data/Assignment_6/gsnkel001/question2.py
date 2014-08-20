#Basic vector calculations
#2014-04-23
#Kelly Goosen
import math
#Getting input vectors
A=(input("Enter vector A:\n"))
B=(input("Enter vector B:\n"))

listA = A.split() #splitting list A
listB = B.split() #splitting list A

def add(): #adding vectos
    listC=[]
    for i in range(3):
        x =eval(listA[i])+eval(listB[i])
        listC.append(x) 
    print("A+B = " , listC, sep='')
add()

def multiply(): #multiplying vectors
    mult=0
    for i in range(3):
        x =eval(listA[i])*eval(listB[i])
        mult+=x 
    print("A.B = " , mult, sep='') 
multiply()    

def normalA(): #squaring vector A, adding and square rooting
    boo=0
    for i in range(3):
        x=(eval(listA[i])**2)
        boo+=x
    p=math.sqrt(boo)
    print("|A| = ", "{0:.2f}".format(p), sep='')
normalA()

def normalB():  #squaring vector B, adding and square rooting
    boo=0
    for i in range(3):
        x=(eval(listB[i])**2)
        boo+=x
    p=math.sqrt(boo)
    print("|B| = ", "{0:.2f}".format(p), sep='')
normalB()
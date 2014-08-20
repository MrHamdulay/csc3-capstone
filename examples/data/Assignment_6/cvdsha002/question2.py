#Shahrain Coovadia
#CVDSHA002
#25/4/14
import math

a=input("Enter vector A:\n")        
b=input("Enter vector B:\n")            # prompt user to enter two vectors

list=a + " " + b
list=list.split(' ')       # add vectors to one list and then split into different strings

def vect(): # define function that calulates sum of vectors
    x=0
    y=3
    sum=[]
    for i in range(3):
        a = int(list[x])
        b = int(list[y])                 #converts strings into integers
        number=((a) + (b))
        sum.append(number)     #adds numbers to list
        x = x+ 1
        y = y+ 1
    print("A+B =", sum)
    
def product():     # define function that calculates product of vectors
    r=0
    s=3
    t=0
    for i in range(3):
        a= list[r]                      #creates new lists
        b= list[s]
        product=int(a)*int(b)
        r=r+1
        s=s+1
        t=t+product
    print("A.B =", t)    
    
def parta():
    start = 0
    d = 0
    for i in range(3):
        sqr = int(list[start])**(2)
        start=start+1
        d=d+sqr
    s = math.sqrt(d)
    print("|A| =", '{0:.2f}'.format(round(s,2)))
    
def partb():
    start = 3
    d = 0
    for i in range(3):
        sqr= int(list[start])**(2)
        start=start+1
        d=d+sqr
    s = math.sqrt(d)
    print("|B| =", '{0:.2f}'.format(round(s,2)))
    
vect()
product()
parta()
partb()

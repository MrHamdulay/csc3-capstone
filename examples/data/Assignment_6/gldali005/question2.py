#This program works out the addition,multiplication and mod of 2 lists
#Ali Goldstein
#24 April 2013

import math

def add(a,b):
    #This function is adding vector A and B tagether and producing a net vector
    added= []
    for i in range(3):
        added.append((eval(a[i])+eval(b[i])))     
    print('A+B = ', added,sep='') 

def product(a,b):
    #This function is working out the product of vector A and vector B
    ans = 0
    for i in range(len(a)):
        ans = ans+eval(a[i])*eval(b[i])
    print("A.B = " , ans, sep='') 

def modA(a):
    #This function is finding the modular value of A
    ans = 0
    for i in range(len(a)):
        ans = ans + eval(a[i])*eval(a[i])
    ans = math.sqrt(ans)   
    print('|A| = ' , '{:.2f}'.format(ans) ,sep='') 
    
def modB(b):
    #This function is finding the modular value of B
    ans = 0    
    for i in range(len(b)):
        ans = ans + eval(b[i])*eval(b[i])
    ans = math.sqrt(ans)
    print("|B| = ", "{:.2f}".format(ans),sep='')
    
def main():
    #This is the main function that calls the other functions 
    #prompts the user to enter the value of the two vectors
    A=[]
    B=[]
    Alist = input("Enter vector A:\n")
    Blist = input("Enter vector B:\n")
    A = Alist.split(" ")
    B = Blist.split(" ")
    #Both of the lines above are saving the values entered in by the user into a list
    add(A,B)
    product(A,B)
    modA(A)
    modB(B)
    
main()
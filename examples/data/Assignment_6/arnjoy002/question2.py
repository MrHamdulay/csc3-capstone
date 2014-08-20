#Joy Arendse-Gorvalla

from math import* #to use the square root function
def add(a,b): #defining a new function
    plus=[] #creating list
    for i in range(3): #loop
        plus.append((eval(a[i])+eval(b[i]))) #adding A and B together and adding it to list
    print('A+B = ', plus,sep='') 

def product(a,b):
    ans = 0
    for i in range(len(a)):
        ans = ans+eval(a[i])*eval(b[i]) #multiplying A and B
    
    print("A.B = " , ans, sep='') 

def SA(a):
    ans = 0
    for i in range(len(a)):
        ans = ans + eval(a[i])*eval(a[i])
       
    ans = round(sqrt(ans),2) #from math library to square root 
    
    print('|A| = ' ,ans ,sep='') 
    
def SB(b):
    
    ans = 0    
    for i in range(len(b)):
        ans = ans + eval(b[i])*eval(b[i])
       
    ans = round(sqrt(ans),2)
    
    print("|B| = ", ans,sep='')
    
def main():
    
    A=[]
    B=[]
    Alist = input("Enter vector A:\n")
    Blist = input("Enter vector B:\n") #asking for user input
    A = Alist.split(" ")
    B = Blist.split(" ") 
    
    add(A,B)
    product(A,B) 
    SA(A)
    SB(B)
    
main() #invoking function
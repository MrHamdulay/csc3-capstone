#CSC1015F 
#ASSIGNMENT 6
#QUESTION 2
#WHTBAS001
#23/04/2014
import math

def vec_addition(a,b):
    c = [0,0,0]
    for i in range(3):
        c[i] = a[i]+b[i]
    print("A+B =",c)
      
def vec_multiplication(a,b):
    c = [0,0,0] #dummy output  
    for i in range(3):
        c[i] = (a[i])*(b[i]) #calcs dot product of each x,y,z
    print("A.B =", c[0]+c[1]+c[2], sep=" ") #prints value of dot product

def mod(a,b):
    moda = math.sqrt(((a[0])**2)+((a[1])**2)+((a[2])**2)) #calculates |A|
    modb = math.sqrt(((b[0])**2)+((b[1])**2)+((b[2])**2)) #calculates |B|
    moda = '{0:1.2f}'.format(moda) #formats |A| to 2 dec places    
    modb = '{0:1.2f}'.format(modb) #formats |B| to 2 dec places    
    print("|A| =", moda, "\n|B| =", modb, sep=" ") #outputs |A| & |B|
    
def main():
    ainput = input("Enter vector A:\n") #A vector input 
    binput = input("Enter vector B:\n") #B vector input
    A = ainput.split() #splits input into array of strings
    B = binput.split() #splits input into array of strings         
    for i in range(3):
        A[i] = eval(A[i]) #converts A string to ints/floats
        B[i] = eval(B[i]) #converts B string to ints/floats        
    vec_addition(A,B) #calls addition function
    vec_multiplication(A,B) #calls dotproduct function
    mod(A,B) #calls mod function

main()
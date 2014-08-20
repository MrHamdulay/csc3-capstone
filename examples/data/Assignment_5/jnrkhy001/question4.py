#Khyati Jinerdeb
#JNRKHY001
#Assignment 5
#15/04/2014

import math
def main():
    
    f_of_x=input("Enter a function f(x):\n")
    
    #use of loops to define the limits 
    for y in range(10,-11,-1):  
        for x in range(-10,11):
            function=eval(f_of_x)
            if y==round(function): #to print the circle
                            print("o",end="")            
            elif x==0 and y==0:
                print("+",end="")
            elif x==0:
                    print("|",end="")  #to get the y axis
            elif y==0:
                print("-",end="")      #to get the x axis
            else:
                print(" ",end="")      #to get the origin
                
        print()
                
main()
                
                 
    
    
    



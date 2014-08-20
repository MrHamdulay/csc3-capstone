#Question3
#Tase Ngambi
import math
def frame():
    
    message = input("Enter the message:\n")
    repeat = eval(input("Enter the message repeat count:\n"))
    thick = eval(input("Enter the frame thickness:\n"))  
    
    width = len(message)      
    
   
    
    if thick != 0:
        print("+","-"*(width+(2*thick)),"+",sep ="")
        for x in range(thick-1):
            print("|"*(x+1),"+","-"*((width+(2*thick)) - 2*(x+1)),"+","|"*(x+1),sep="")
    
   
    for i in range(repeat):
        print("|"*(thick-1),end ="")
        print("|"," ",message," ", "|" ,sep ="", end ="")
        print("|"*(thick-1))
    
    
    
    if thick != 0:
        for x in range(thick-1):
            print("|"*(thick-(x+1)),"+","-"*((width) + 2*(x+1)),"+","|"*(thick-(x+1)),sep="")

        print("+","-"*(width+(2*thick)),"+",sep ="")
    
                  
    
    





     
frame()
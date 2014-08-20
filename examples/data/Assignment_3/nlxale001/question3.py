#Author: NLXALE001
#Date: 27 March 2014
#Assignment 3

mess = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))

if rep!=0 and thick !=0:
    dash = len(mess)+(2*thick)
    print("+" , "-"*dash , "+" , sep="")
    line = 1
    for x in range (1, thick):
        dash = dash-2
        print ("|"*line , "+" , "-"*dash , "+" , "|"*line, sep="")
        line = line+1
        
    for y in range(0, rep):
        print ("|"*thick , mess , "|"*thick)
         
    line = thick-1
    for x in range (1, thick):
        print ("|"*line , "+" , "-"*dash , "+" , "|"*line, sep="")
        line = line-1 
        dash = dash+2
    print("+" , "-"*dash , "+" , sep="")    
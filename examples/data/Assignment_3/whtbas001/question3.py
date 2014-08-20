#WHTBAS001
#ASSIGNMENT 3
#QUESTION 3
#25-03-2014

def frame(a,b,c):
    lena = len(a)
    lvert = b +2*c #number repeats and twice the thickness
    lhoriz = lena + 2*c  #length of message, dbl thickness + 2 spaces
    #Top section (frame)
    for i in range(c):
        print("|"*i,"+","-"*(lhoriz-2*i),"+","|"*i,sep="", end="\n")
    #Middle section (body)
    for k in range(b):
        print("|"*c,a,"|"*c, sep=" ", end="\n")
    #Bottom section (frame)
    for j in range(c):
        print("|"*(c-j-1),"+","-"*(lhoriz-2*(c-j-1)),"+","|"*(c-j-1),sep="", end="\n")                
    
message = input("Enter the message:\n")
repeat = int(eval(input("Enter the message repeat count:\n")))
thickness = int(eval(input("Enter the frame thickness:\n")))

frame(message, repeat, thickness)

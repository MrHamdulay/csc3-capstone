# 23 March 2014
# Program to frame an input message
# by Nomsa Gamedze

def frame():
    message = input("Enter the message:"'\n')
    width = len(message)
    repeat = eval(input("Enter the message repeat count:"'\n'))
    thickness = eval(input("Enter the frame thickness:"'\n'))
    if thickness != 0 and repeat !=0:
        print("+", "-"*(width+(2*thickness)), "+", sep="")
    
        for j in range(thickness-1):
            print("|"*(j+1), "+", "-"*(width+(2*(thickness-j))-2), "+", "|"*(j+1), sep="")
    
        for i in range(repeat):
            print("|"*thickness, message, "|"*thickness)
    
        for e in range(thickness-1, 0, -1):
            print("|"*(e), "+", "-"*(width + (2*(thickness-e))), "+", "|"*(e), sep="")

        print("+", "-"*(width+2*thickness), "+", sep="")    

frame()
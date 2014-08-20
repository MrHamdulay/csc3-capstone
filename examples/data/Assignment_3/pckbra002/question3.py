#draw a frae around a message
#Assignment 3 Question 3
#Brandon Pickup - PCKBRA002
#19 March 2014
message = " "+input("Enter the message:\n")+" "
repeat = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
count=0
line=0
dash=len(message)+(thick-1)*2 
while (count<thick):
    print("{0}{1}{2}{1}{0}".format("|"*(line),"+","-"*(dash)))
    dash-=2
    line+=1
    count+=1
else:
    for i in range(repeat):
        print("{0}{1}{0}".format("|"*thick,message))   
while (count>0):
    dash+=2
    line-=1
    count-=1    
    print("{0}{1}{2}{1}{0}".format("|"*(line),"+","-"*(dash)))
    
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

line = frame
linesub = line #Amount of |'s to be added
n = 0 #Amount of -'s to be subtracted

#-----------------------------------------------------------------------------
if repeat > 0 and frame > 0:
    print("+","-"*((len(message)+(frame)+frame)),"+",sep="") #Top line

for i in range(frame-1):
    print("|"*((line-(linesub-1))),"+","-"*((len(message)+(frame - 2)+frame)-n),"+","|"*((line-(linesub-1))),sep="")
    linesub -= 1
    n += 2

#-----------------------------------------------------------------------------

for i in range(repeat):    
    print("|"*frame," ",message," ","|"*frame,sep="") #Message

#-----------------------------------------------------------------------------

linesub += 1
n -= 2

for i in range(frame):
    print("|"*((line-(linesub-1))),"+","-"*((len(message)+(frame - 2)+frame)-n),"+","|"*((line-(linesub-1))),sep="")
    linesub += 1
    n -= 2
    
#print("+","-"*((len(message)+(frame)+frame)),"+",sep="") #Bottom line

#-----------------------------------------------------------------------------
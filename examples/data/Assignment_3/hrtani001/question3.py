message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
if repeat and thickness != 0:
    print("+","-"*(len(message)+(thickness*2)),"+",sep="")
    for i in range(1,thickness,1):
        print("|"*(i),"+","-"*(len(message)+(thickness*2)-2*i),"+","|"*(i),sep="")
        i+=1
    for i in range(0,repeat):
        print("|"*thickness,message,"|"*thickness)
    for i in range(thickness,1,-1):
        print("|"*(i-1),"+","-"*(len(message)+(thickness-i)*2+2),"+","|"*(i-1),sep="")
        i+=1
    print("+","-"*(len(message)+(thickness*2)),"+",sep="")
message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
width=eval(input("Enter the frame thickness:\n"))
line=0
thickness=width*2+len(message)
for i in range(width):
    print("|"*line,"+","-"*thickness,"+","|"*line,sep="")
    line=line+1
    thickness=thickness-2
for i in range(1,repeat+1):
    print("|"*width,message,"|"*width)
line=width-1
thickness=thickness+2
for i in range(width):
    print("|"*(line),"+","-"*thickness,"+","|"*(line),sep="")
    line=line-1
    thickness=thickness+2
    
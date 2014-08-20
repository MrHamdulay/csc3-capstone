message=input("Enter the message:""\n")
rcount=eval(input("Enter the message repeat count:""\n"))
thickness=eval(input("Enter the frame thickness:""\n"))

for i in range(thickness):
    print("|"*(i),"+","-"*(len(message)+(2*thickness)-(2*i)),"+","|"*(i),sep="")

for j in range(rcount):
    print("|"*thickness,message,"|"*thickness)

for k in reversed(range(thickness)):
    print("|"*(k),"+","-"*(len(message)+(2*thickness)-(2*k)),"+","|"*(k),sep="")

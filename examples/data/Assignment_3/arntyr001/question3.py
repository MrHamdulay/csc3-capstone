message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
a=len(message)+2
b=repeat
c=2*(thick-1)
d=thick
e=0
for i in range(thick):
    print("|"*(i),"+","-"*(a+c),"+","|"*(i),sep="")
    c=c-2
for i in range(repeat):  
    print("|"*thick,message,"|"*thick)
for i in range(d,0,-1):
    print("|"*(i-1),"+","-"*(a+e),"+","|"*(i-1),sep="")
    e=e+2
message = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
x=len(message) + frame*2
y=0
a=frame
z=len(message) + 2
while frame != 0:
    print("|"*y,"+", "-"*x, "+","|"*y,sep="")
    x-=2
    frame-=1
    y+=1
while rep != 0:
    print("|"*a," ", message," ","|"*a,sep="")
    rep-=1
while a!= 0:
    p=a-1
    if a == 1:
        print("+", "-","-"*(z-2),"-", "+",sep="")
    else:
        print("|"*p,"+", "-"*z, "+","|"*p,sep="")
    z+=2
    a-=1
   
      

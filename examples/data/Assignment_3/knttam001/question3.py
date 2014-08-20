m = input("Enter the message:\n")
c = eval(input("Enter the message repeat count:\n"))
t = eval(input("Enter the frame thickness:\n"))
C = len(m)+2
for i in range(t):
    print("|"*i,"+","-"*(C+ t*2 -2),"+","|"*i,sep="")
    C-=2
for x in range(c):
    print("|"*t," ",m," ","|"*t,sep="")
C = len(m) +2
for i in range(t-1,-1,-1):
    print("|"*i,"+","-"*(C),"+","|"*i,sep="")
    C+=2


m=input("Enter the message:\n")
repC=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))

dash=len(m)+2*t
for i in range(t):
    print("|"*i,"+","-"*dash,"+","|"*i, sep="")
    dash=dash-2
    
for i in range(repC):
    print("|"*t, m,"|"*t)

dash=len(m)+2
for i in range(t,0,-1):
    print("|"*(i-1),"+","-"*dash,"+","|"*(i-1), sep="")
    dash=dash+2
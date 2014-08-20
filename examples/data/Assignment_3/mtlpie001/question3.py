
x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
A=eval(input("Enter the frame thickness:\n"))
for i in range(A):
    print("|"*(i)+"+"+"-"*(len(x)+2*(A-i))+"+"+"|"*(i))
for i in range(y):
    print("|"*A,x,"|"*A)
for i in range(A-1,-1,-1):
    print("|"*(i)+"+"+"-"*(len(x)+2*(A-i))+"+"+"|"*(i))   

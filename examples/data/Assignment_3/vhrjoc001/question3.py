a=input("Enter the message:\n")
b=eval(input("Enter the message repeat count:\n"))
c=eval(input("Enter the frame thickness:\n"))
d=len(a)
e=0
f=c-1
for i in range(c):
  print("|"*e,"+","-"*(d+(2*(c))),"+","|"*e,sep="")
  e=e+1
  d=d-2
for i in range(b):
  print("|"*c,a,"|"*c)
l=len(a)+2
for i in range(c):
    print("|"*(f),"+","-"*(l),"+","|"*(f),sep="")
    f=f-1
    l=l+2  
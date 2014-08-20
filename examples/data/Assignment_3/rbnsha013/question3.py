print("Enter the message:")
w = input()
print("Enter the message repeat count:")
r = eval(input())
print("Enter the frame thickness:")
t = eval(input())
temp = t
p = 1
if r==0 and t==0:
    print()
else:
    print("+","-"*(len(w)+2*t),"+",sep="")
for i in range(0,t-1):
    print("|"*p,"+","-"*(len(w)+2*t-2*p),"+","|"*p,sep="")
    p+=1
for i in range(0,r):
    print("|"*t," ",w," ","|"*t,sep="")
p = t-1
for i in range(0,t-1):
    print("|"*p,"+","-"*(len(w)+2*t-2*p),"+","|"*p,sep="")
    p-=1
    temp+=1
if r==0 and t==0:
    print()
else:
    print("+","-"*(len(w)+2*t),"+",sep="")
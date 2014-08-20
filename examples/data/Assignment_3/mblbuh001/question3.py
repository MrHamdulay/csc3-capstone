# question3.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 March 2014

x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

d = z
for i in range (z):
    print("|"*i,end='')
    print("+"+"-"*(d*2+len(x))+"+",end='')
    print("|"*i)
    d-=1
    #Top part
for j in range(y):
    print("|"*z,x,"|"*z)
    #Middle part
e = 0
for k in range(z):
    print("|"*(z-k-1),end='')
    print("+"+"-"*(e*2+len(x)+2)+"+",end='')
    print("|"*(z-k-1))
    e+=1
    #Bottom part
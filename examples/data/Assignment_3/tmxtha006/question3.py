#This program frames a message
#Name: TEMA, Thabo Hebert
#Student no.: TMXTHA006
#Date: 20 March 2014

x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

l=len(x)
d = l+(2*z)
s = 0
D = l+2
S = z-1
for i in range(z):
    print("|"*s, "+", "-"*d, "+", "|"*s, sep="")
    s+=1
    d-=2
for a in range(y):
    print("|"*z, x, "|"*z, sep=" ")
for j in range(z):
    print("|"*S, "+", "-"*D, "+", "|"*S, sep="")
    S-=1
    D+=2
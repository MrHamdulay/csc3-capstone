x = input("Enter the message:\n")
b = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

g = z
f = len(x)
h = f+ g + (g)
er = g
re=er
po=f+2


for i in range(z):
    print('|'*(z-1 -(g-1)), end='')
    print('+',end='')
    print('-'*(h), end='')
    print('+', end='')
    print('|'*(z-1-(g-1)))
    z = z+1
    h = h-2

    

for i in range(b):
    print('|'*g,x,'|'*g)
    
for i in range(er):
    print("|"*(er-1),end='')
    print('+', end='')
    print('-'*po,end='')
    print('+',end='')
    print('|'*(er-1))
    
    po=po+2    
    er = er-1

#Author: Lenard Carroll
#Student Number: CRRLEN001
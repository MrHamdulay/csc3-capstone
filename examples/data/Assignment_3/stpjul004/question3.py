# Question 3 | Assignment 3
# Author: Julius Stopforth (STPJUL004)
# Date: 20/03/2014

msg = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))

for i in range(0,thick):
    print('|'*i,'+','-'*(len(msg)+2*(thick-i)),'+','|'*i,sep='')

for j in range(repeat):
    print('|'*thick,' ',msg,' ','|'*thick,sep='')
    
for i in range(thick-1,-1,-1):
    print('|'*(i),'+','-'*(len(msg)+2*(thick-i)),'+','|'*(i),sep='')
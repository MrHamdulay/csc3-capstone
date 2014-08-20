# Author: Raees Eland
# Question 3: Printing a border around a messege.
# 25 March 2014

s=input('Enter the message:\n')
y=eval(input('Enter the message repeat count:\n'))
x=eval(input('Enter the frame thickness:\n'))
t=1
z=0
q=0
w=x
for i in range(x):
    print('|'*(x-w),'+','-'*(len(s)+(x*2)+q),'+','|'*(x-w),sep='')
    w-=1
    q-=2
for i in range(y):
    print('|'*x,s,'|'*x) 
for i in range(x):
    print('|'*(x-t),'+','-'*(len(s)+(z+2)),'+','|'*(x-t),sep='')
    t+=1
    z+=2

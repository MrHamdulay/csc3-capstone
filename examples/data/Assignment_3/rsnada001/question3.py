#Adam Rosendorff
#RSNADA001
#CSC1015F - Assignment 3 - Question 3
mes = input('Enter the message:\n')
count = eval(input('Enter the message repeat count:\n'))
thick = eval(input('Enter the frame thickness:\n'))
for i in range(thick):
    print('|'*i,'+','-'*(len(mes)+2),'-'*(thick*2-2-2*i),'+','|'*i,sep='')
for i in range(count):
    print('|'*thick,mes,'|'*thick)
for i in range(thick-1,-1,-1):
    print('|'*i,'+','-'*(len(mes)+2),'-'*(thick*2-2-2*i),'+','|'*i,sep='')


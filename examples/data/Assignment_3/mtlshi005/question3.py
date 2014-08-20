#19/03/14
#Shivaan Motilal
#Programme to create a triangle

x=input('Enter the message:\n')
r=eval(input('Enter the message repeat count:\n'))
f=eval(input('Enter the frame thickness:\n'))

l=len(x)+4      

for i in range(f-1,-1,-1):
    
    m=(f-1)-i
    print(m*'|','+',i*'-','-'*(len(x)+2),i*'-','+',m*'|',sep='')

for i in range(r):
    print(f*'|',x,f*'|')
    


for i in range(f):
    j=(f-1)-i
    print(j*'|','+',i*'-','-'*(len(x)+2),i*'-','+',j*'|',sep='')


   
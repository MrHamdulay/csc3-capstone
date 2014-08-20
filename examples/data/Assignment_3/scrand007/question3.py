message = input('Enter the message:\n')
repeat = eval(input('Enter the message repeat count:\n'))
thick = eval(input('Enter the frame thickness:\n'))
x=0
a=(thick-1)
y=0
z=0
b=(thick-1)
f=0

while x<thick:
    print(x*'|','+','-'*(len(message)+2*a+2),'+',x*'|',sep='')
    x+=1
    a-=1

while y<repeat:
    print(thick*'|',' ',message,' ',thick*'|',sep='')
    y+=1
    
while z<thick:
    print(b*'|','+','-'*(len(message)+2+f),'+',b*'|',sep='')
    z+=1
    b-=1
    f+=2
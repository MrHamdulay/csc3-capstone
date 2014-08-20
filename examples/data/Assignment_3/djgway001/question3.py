#message surrounded by border

mes=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))

a=len(mes)+2
b=a+2*thick

#upside down triangle
gap=0
for i in range(b,a,-2):
    print('|'*gap,end='')
    print("+",end='')
    print("-"*(i-2),end='')
    print("+",end='')
    print('|'*gap)
    gap=gap+1

#middle message
for i in range(0,repeat,1):
    print("|"*thick,mes,"|"*thick)

#upright triangle
gap=thick-1
for i in range(a,b,2):
    print('|'*gap,end='')
    print("+",end='')
    print("-"*i,end='')
    print("+",end='')
    print('|'*gap)
    gap=gap-1
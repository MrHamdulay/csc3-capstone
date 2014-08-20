message = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
a=len(message)+2*thickness
b=len(message)+2
gap = 0
for i in range(a,b-2,-2):
    print('|'*gap,'+','-'*i,'+','|'*gap,sep="")
    gap=gap+1
for h in range(y):
    print('|'*thickness, message.center(a-2*thickness),'|'*thickness)
gap = thickness - 1
for l in range(b, a+1, 2):
    print('|'*gap,'+','-'*l,'+','|'*gap, sep="")
    gap = gap - 1
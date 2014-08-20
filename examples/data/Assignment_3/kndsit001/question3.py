message = input("Enter the message:\n")
base = 0
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
dash = (len(message)+2)

for i in range(1,thickness,1):
    dash+=2
for a in range(thickness):
    print(base*"|","+","-"*dash,"+",base*"|",sep="")
    base+=1
    dash-=2
for b in range(repeat):
    print(thickness*"|",message,"|"*thickness)
for c in range(thickness):
    base-=1
    dash+=2
    print(base*"|","+","-"*dash,"+",base*"|",sep="")
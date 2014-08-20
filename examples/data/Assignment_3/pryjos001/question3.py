#Program to draw a frame around repeated words

message=input("Enter the message:\n")

repeat=eval(input("Enter the message repeat count:\n"))

thick=eval(input("Enter the frame thickness:\n"))

space = thick

length = len(message)

#Print outermost layer of frame
if thick>0:
    print ("+", (length+(2*thick))*"-", "+", sep="")

#print inner parts of the frame

inner = thick-1

while inner>0:
    print ((thick-inner)*"|", "+", (length+(2*inner))*"-", "+", (thick-inner)*"|", sep="")
    inner-=1

for j in range(0,repeat):
    print(thick*"|", message, thick*"|")

inner = thick-1

while inner>0:
    print (inner*"|", "+", (length+(2*(thick-inner)))*"-", "+", inner*"|", sep="")
    inner-=1
    
if thick>0:
    print ("+", (length+(2*thick))*"-", "+", sep="")
message = input("Enter the message: \n")
count = eval(input("Enter the message repeat count: \n"))
frame = eval(input("Enter the frame thickness: \n"))
line=0
dashes = len(message) + frame*2  
for i in range(frame, 0, -1):
    print("|"*line, "+", "-"* dashes,"+", "|"*line, sep="")
    dashes=dashes-2
    line=line+1
    
for i in range(count):
    print("|"*frame, message, "|"*frame)
    
dashes = len(message) +2     
line= frame-1
for i in range(0, frame, 1):
    print("|"*line, "+", "-"* dashes,"+", "|"*line, sep="")
    dashes=dashes+2
    line=line-1

            
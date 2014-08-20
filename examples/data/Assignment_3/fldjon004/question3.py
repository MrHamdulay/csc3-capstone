message = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

top = 1
bottom = frame - 1

if frame>0:
    print("+", "-"*(len(message)+frame*2), "+", sep="")
    for t in range(frame-1):
        print("|"*top, "+", "-"*(len(message)+frame*2-top*2), "+", "|"*top, sep="")
        top = top +1
    
for i in range(count):
    print("|"*frame,message, "|"*frame)
    
if frame>0:
    for s in range(frame-1):
        print("|"*bottom, "+", "-"*(len(message)+frame*2-bottom*2), "+", "|"*bottom, sep="")
        bottom = bottom - 1
    print("+", "-"*(len(message)+frame*2), "+", sep="")
    
        
        
        
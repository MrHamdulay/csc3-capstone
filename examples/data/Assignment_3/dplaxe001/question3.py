message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
mesLength = len(message)
sideFrame = 0
for i in range(frame):
    print("|"*(i)+"+"+"-"*((mesLength+(frame*2))-(i*2))+"+"+"|"*(i))
    sideFrame = i

for i in range(repeat):
    print("|"*(sideFrame+1), message, "|"*(sideFrame+1))
    
for i in range(frame,0,-1):
    print("|"*(i-1)+"+"+"-"*((mesLength+(frame*2))-((i*2)-2))+"+"+"|"*(i-1))
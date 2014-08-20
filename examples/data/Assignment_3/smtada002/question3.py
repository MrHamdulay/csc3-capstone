message = input("Enter the message:\n")
repeatCount = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

length = len(message)

for i in range (0, frame):
    print("|"*i+"+" + "-"*(length+(frame-i)*2) +"+"+"|"*i)

for i in range (0, repeatCount):
    print("|"*frame, message, "|"*frame, end = "\n")
    
for i in range (frame-1, -1, -1):
    print("|"*i+"+" + "-"*(length+(frame-i)*2) +"+"+"|"*i)
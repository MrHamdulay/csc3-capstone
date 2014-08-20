
message = input("Enter the message:\n")
repeatCount = eval(input("Enter the message repeat count:\n"))
frameThick = eval(input("Enter the frame thickness:\n"))
messageLength = len(message)

#Prints top part of the frame
for i in range(frameThick):
    dashes = "-"*((messageLength+(frameThick*2)-(i*2)))
    print("|"*i + "+" + dashes + "+" + "|"*i)

#Middle part where message is    
for j in range(repeatCount):
    print("|"*(i+1) ,message, "|"*(i+1))
    
#Prints bottom part of the frame
for k in range(frameThick):
    dashes = "-"*((messageLength+2+(k*2)))
    print("|"*(i-k) + "+" + dashes + "+" +  "|"*(i-k))
    

    

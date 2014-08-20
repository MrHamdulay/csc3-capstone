message = input("Enter the message:\n") # Input message
repCount = eval(input("Enter the message repeat count:\n"))# Input message repeat count
frameThick = eval(input("Enter the frame thickness:\n")) # Input frame thickness

bigWidth = (len(message)+2)+(frameThick*2)
counter = 0
lines = 0
dash = bigWidth-2
for i in range (frameThick):
    while counter < frameThick:
        print(("|"*lines)+("+")+("-"*dash)+("+")+("|"*lines))
        counter = counter+1
        lines = lines+1
        dash = dash-2
    

for i in range (repCount):
    print(("|"*frameThick),message,("|"*frameThick)) # Prints lines and message
    
smallWidth = len(message)+2
lines2 = frameThick-1
for i in range (frameThick):
    print(("|"*lines2)+("+")+("-"*smallWidth)+("+")+("|"*lines2))
    lines2 = lines2-1
    smallWidth = smallWidth+2
    
    

    
    
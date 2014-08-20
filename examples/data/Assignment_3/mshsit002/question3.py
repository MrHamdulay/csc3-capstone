message = input("Enter the message:\n")
repeatCount = eval(input("Enter the message repeat count:\n"))
frameThick = eval(input("Enter the frame thickness:\n"))
messageLength = len(message)

topLength = (frameThick*2)+messageLength


#Prints top part of the frame
j = 0
for i in range(topLength,messageLength,-2):
    dashes = "-"*i
    print("|"*j + "+" + dashes + "+" + "|"*j)
    j += 1


#Middle part where message is    
for x in range(repeatCount):
    print("|"*(j) ,message, "|"*(j))
    
  
#Prints bottom part of the frame
l=1  
for k in range(messageLength+2,topLength+1,2):
    dashes = "-"*k
    print("|"*(j-l) + "+" + dashes + "+" +  "|"*(j-l))
    l+=1
    

    

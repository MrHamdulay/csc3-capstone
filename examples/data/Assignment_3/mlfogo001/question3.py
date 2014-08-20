message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))

for i in range(frame):
    print(("|"*i)+("+")+(("-"*((len(message)+(2*frame))-(i+i))+("+")+("|"*i))))                            

for i in range(repeat):
    print(("|"*frame)+ (" "+message+" ") + ("|"*frame))
    
for i in range(frame-1,-1,-1):
    print(("|"*(i))+("+")+(("-"*((len(message)+(2*frame))-(i+i))+("+")+("|"*i))))    

message=input("Enter the message:\n")

repeat=eval(input("Enter the message repeat count:\n"))

frame=eval(input("Enter the frame thickness:\n"))
message
x = len(message)
y = x + frame*2 
z = 0
for j in range(frame):
    print("|"*z + "+" + y*"-" + "+" + "|"*z)
    y = y - 2
    z += 1

for i in range(repeat):
    print("|"*frame,message,"|"*frame)
    
y = y + 2
z = z-1
    
for j in range(frame):
         
    print("|"*z + "+" + y*"-" + "+" + "|"*z)
    y = y +2
    z = z - 1








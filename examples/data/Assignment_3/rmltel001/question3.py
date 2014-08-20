#Draw a frame

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
k = 0
j = thickness
for i in range(thickness, 0, -1):
    print("|"*k,"+", "-"*(len(message)+(i*2)), "+", "|"*k, sep = "")
    k+=1

for i in range(repeat):
    print("|"*thickness + " " + message + " " + "|"*thickness, sep = "")
    
for i in range(0, thickness):
    print("|"*(j-1),"+", "-"*(len(message)+((i)*2)+2), "+", "|"*(j-1), sep = "")
    j-=1
    
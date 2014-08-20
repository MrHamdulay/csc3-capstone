# Frame
# Sofia Palmer
# 24/3/14

message = input("Enter the message:\n")
repeat_count = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
width = len(message)
dash = (frame * 2)
for j in range(0,frame):
    print("|" * j,"+",(dash + width) * "-","+","|" * j,sep="")
    dash = dash - 2
for i in range(1,repeat_count+1):
    print((frame * "|"), message, (frame * "|"))

for j in range(frame-1,-1,-1):  
    dash = dash + 2
    print("|" * j,"+",(dash + width) * "-","+","|" * j,sep="")
   
   

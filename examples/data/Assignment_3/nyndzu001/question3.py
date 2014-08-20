message = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
dash = 0
minus = len(message)+2*frame
for i in range(0,frame,1):
    print("|"*dash,"+","-"*minus,"+","|"*dash,sep="")
    dash +=1
    minus -=2
    
dash -= 1
minus +=2

for i in range(0,count,1):
    print("|"*frame,message,"|"*frame)

for i in range(0,frame,1):
    print("|"*dash,"+","-"*minus,"+","|"*dash,sep="")
    dash -=1
    minus +=2
word = input("Enter the message:\n")
message = " "+word+" "
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

line = 0
c = "+"
dash =len(word)+(frame*2)
i = 0

while i < frame:
    print(line*"|", c, dash*"-", c, line*"|", sep="")
    line+=1
    dash-=2
    i+=1
    
line-=1
dash+=2
n = 0
while n < repeat:
    print(frame*"|", message, frame*"|", sep="")
    n+=1
    
while i > 0:
    print(line*"|", c, dash*"-", c, line*"|", sep="")
    line-=1
    dash+=2
    i-=1
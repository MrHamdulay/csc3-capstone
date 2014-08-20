message = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

line1 = 0
line2 = len(message)+2+(frame+frame-2)

for a in range(0,frame):
    print("|"*line1, end="")
    print("+", end="")
    print("-"*line2, end="")
    print("+", end="")
    print("|"*line1)
    line1 = line1 + 1
    line2 = line2-2

for i in range(0, count):
    lines = "|"*frame
    print(lines, message, lines, sep=" ")
    
line3 = frame - 1
line4 = len(message)+2
    
for b in range(0,frame):
    print("|"*line3, end="")
    print("+", end="")
    print("-"*line4, end="")
    print("+", end="")
    print("|"*line3)
    line3 = line3 - 1
    line4 = line4 + 2    
    
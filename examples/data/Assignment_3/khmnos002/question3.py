word = input("Enter the message: \n")
repeat = eval(input("Enter the message repeat count: \n"))
frame = eval(input("Enter the frame thickness: \n"))
length = len(word) + (2*frame)
height = repeat + (2 * frame)
dash = 0
for i in range(frame):
    print("|" * dash, "+", "-" * length, "+", "|" * dash, sep = "")
    dash+=1
    length-=2
for i in range(repeat):
    print("|"*frame, " ", word, " ", "|"*frame, sep = "")

dash = frame - 1
length = len(word) + 2
for i in range(frame):
    print("|"*dash, "+", "-"* length, "+", "|"*dash, sep = "")
    length+=2
    dash-=1
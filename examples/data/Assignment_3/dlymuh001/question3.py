message = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
height = 2*thick + count
width = 2*thick + len(message) + 2
for i in range(1, height+1, 1):
    if (i <= thick):
        print("|"*(i-1) + "+" + "-"*(width - 2*i) + "+" + "|"*(i-1))
    elif (i > thick) and (i <= height - thick):
        print("|"*thick, message, "|"*thick, sep=" ")
    elif (i > height - thick):
        num_bars = height - i
        box_width = width - 2*num_bars - 2
        print("|"*num_bars + "+" + "-"*box_width + "+" + "|"*num_bars)
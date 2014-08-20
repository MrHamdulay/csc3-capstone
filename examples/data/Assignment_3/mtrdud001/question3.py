
def frame(people, counting, width):
    for j in range(width):
        print("|"*j,"+", "-"*(len(people)+(2*(width-j))), "+", "|"*j, sep="")
    for i in range(counting):
            print("|"*width, people,"|"*width)
    for j in range(width-1,-1,-1):
        print("|"*j,"+", "-"*(len(people)+(2*(width-j))), "+", "|"*j, sep="")    
a = input("Enter the message:\n")
repeatcount = eval(input("Enter the message repeat count:\n"))
framewidth = eval(input("Enter the frame thickness:\n"))
frame(a, repeatcount, framewidth)
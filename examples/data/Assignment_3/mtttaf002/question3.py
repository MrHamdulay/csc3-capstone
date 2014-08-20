#creating a frame for given text
#created by tafara mtutu
#21 march 2013
def frame(word, count, thickness):
    for j in range(thickness):
        print("|"*j,"+", "-"*(len(word)+(2*(thickness-j))), "+", "|"*j, sep="")
    for i in range(count):
            print("|"*thickness, word,"|"*thickness)
    for j in range(thickness-1,-1,-1):
        print("|"*j,"+", "-"*(len(word)+(2*(thickness-j))), "+", "|"*j, sep="")    
message = input("Enter the message:\n")
repeat_count = eval(input("Enter the message repeat count:\n"))
frame_thickness = eval(input("Enter the frame thickness:\n"))
frame(message, repeat_count, frame_thickness)
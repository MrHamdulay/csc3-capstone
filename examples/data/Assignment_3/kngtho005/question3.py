# question2.py
# Write a program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines.  
# There is a space before and after the message, and no spaces between concentric boxes.
# Thomas Konigkramer
# 19 March 2014

def framing():
    
    text = input("Enter the message: \n")
    
    reps = eval(input("Enter the message repeat count: \n"))
    
    frame = eval(input("Enter the frame thickness: \n"))
    
    length = len(text) + frame * 2
    verticals = 0
    for a in range(frame):
        print(verticals * "|", "+", length * "-", "+", verticals * "|", sep = "")
        length -= 2
        verticals += 1
    
    for b in range(reps):
        print("|" * frame, text, "|" * frame)
    
    newlength = len(text) + 2
    newverticals = frame - 1
    for c in range(frame):
            print(newverticals * "|", "+", newlength * "-", "+", newverticals * "|", sep = "")    
            newlength += 2
            newverticals -= 1
            
framing()
#Assignment 3
#Question 3

def printing():
    message = input("Enter the message: \n")
    repeat = eval(input("Enter the message repeat count: \n"))
    frame = eval(input("Enter the frame thickness: \n"))
    i = 0
    j = 0
    c = frame - 1
    while i < frame:
        print('|'*i,'+','-'*(2*c+2+len(message)),'+','|'*i,sep='')
        c -= 1
        i += 1
    while j < repeat:
        print('|'*frame,' ',message,' ','|'*frame,sep='')
        j += 1
        c = 0
    while i > 0:
        i -= 1
        print('|'*i,'+','-'*(2*c+2+len(message)),'+','|'*i,sep='')
        c += 1
                
    

printing()
#Thembekani Gwegwana
#GWGTHE001
#A program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines.  There is a space before and after the message, and no spaces between concentric boxes.

def frame():
    message=input('Enter the message:\n')
    repeat_message=eval(input('Enter the message repeat count:\n'))
    framethickness=eval(input('Enter the frame thickness:\n'))
    for i in range(framethickness):
        print('|'*i,'+','-'*(len(message)),'-'*2*(framethickness-i),'+', '|'*i,sep='')
    for i in range(repeat_message):
        print('|'*framethickness, message, '|'*framethickness)
    for i in range(framethickness-1,-1,-1):
                print('|'*i,'+','-'*(len(message)),'-'*2*(framethickness-i),'+', '|'*i,sep='')    
frame()
# A program that prints a string a set number of times in a frame
#Jason Findlay
#28/03/2014

message=input('Enter the message:\n')
frame=eval(input('Enter the frame thickness:\n'))
message=' '+message+' '
count=eval(input('Enter the message repeat count:\n'))

def border(i,frame):
    while i<frame:
        print('+','-'*(len(message)+2*(frame-i)),'+')
        i+=1
border(0,frame)

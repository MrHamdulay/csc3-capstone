__author__ = 'User1'
def roof(FrameWidth,StringLength):
    k = StringLength + 2*FrameWidth
    i = 0
    while k>StringLength:

        print("|"*i+"+"+"-"*k+"+"+"|"*i)
        k -= 2
        i += 1

def floor(FrameWidth,StringLength):
    k = StringLength+2
    i = FrameWidth - 1
    while i+1 != 0:
        print("|"*i+"+"+"-"*k+"+"+"|"*i)
        i -= 1
        k += 2
message = input("Enter the message:\n")
Word_repeat_count = eval(input("Enter the message repeat count:\n"))
FrameWidth = eval(input("Enter the frame thickness:\n"))

roof(FrameWidth,len(message))

while Word_repeat_count>0:
    print("|"*(FrameWidth),message,"|"*(FrameWidth))
    Word_repeat_count-=1
floor(FrameWidth,len(message))


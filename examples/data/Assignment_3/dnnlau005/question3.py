message=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))

length=len(message)+frame*2

def top():
    for i in range(frame):
        print("|"*i+"+"+"-"*(length-2*i)+"+"+"|"*i)

def middle():
    for i in range(count):
        print("|"*frame+" "+message+" "+"|"*frame)

def bottom():
    for i in range(frame-1,-1,-1):
        print("|"*i+"+"+"-"*(length-2*i)+"+"+"|"*i)

top()
middle()
bottom()
        
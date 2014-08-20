# The Third Question
# MSHMUT003

msg=input("Enter the message:\n")
red=eval(input("Enter the message repeat count:\n"))
swl=eval(input("Enter the frame thickness:\n"))
def frameIT():
    ln=swl
    e=0
    for i in range(swl):
        print("|"*i+"+"+"-"*(len(msg)+2*(swl-i))+"+"+"|"*i)
    for i in  range(red):
        print("|"*swl,msg,"|"*swl)
    for i in range(swl-1,-1,-1):
        print("|"*i+"+"+"-"*(len(msg)+2*(swl-i))+"+"+"|"*i)      
frameIT()
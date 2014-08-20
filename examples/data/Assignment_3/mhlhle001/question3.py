def main():
    msg=input("Enter the message:\n")
    rpc=eval(input("Enter the message repeat count:\n"))
    frt=eval(input("Enter the frame thickness:\n"))
    y=len(msg)+2*frt
    for i in range(frt):
        print(i*"|"+"+"+"-"*y+"+"+"|"*i)
        y-=2
    for i in range(rpc):
        print("|"*frt+" "+msg+" "+"|"*frt)
    y=len(msg)+2
    for i in range(frt,0,-1):
        print("|"*(i-1)+"+"+"-"*y+"+"+"|"*(i-1))
        y+=2
main()
        
        
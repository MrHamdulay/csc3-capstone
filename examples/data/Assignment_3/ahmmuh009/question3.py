def main():
    message=input("Enter the message:\n")
    repeat=int(input("Enter the message repeat count:\n"))
    thickness=int(input("Enter the frame thickness:\n"))
    x=len(message)
    char=""
    for i in range (thickness):
        print(char+"+"+"-"*(x+(2*thickness))+"+"+char)
        char+="|"
        x-=2
    for k in range (repeat):
        print(char+" "+message+" "+char)
    str_1=char
    n=len(char)-1
    x=len(message)
    for j in range (thickness):
        print(str_1[0:n]+"+"+"-"*(x+2)+"+"+str_1[0:n])
        x+=2
        n-=1    
main()
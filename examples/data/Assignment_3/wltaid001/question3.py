#Aiden Walton
#WLTAID001
#Program to draw frame around message

def frame():
    for i in range(1,x+1):
        print("|"*(i-1),end="")
        print("+","-"*(len(word)+4+(2*(x-1))-(i*2)),"+",sep="",end="")
        print("|"*(i-1))
        
    for l in range(0,y):
        print("|"*(i),end="")
        print("",word,"",end="")
        print("|"*(i))
        
    for i in range(x,0,-1):
        print("|"*(i-1),end="")
        print("+","-"*(len(word)+4+(2*(x-1))-(i*2)),"+",sep="",end="")
        print("|"*(i-1))
        
        
if __name__=="__main__":
    word=input("Enter the message:\n")
    y=int(input("Enter the message repeat count:\n"))
    x=int(input("Enter the frame thickness:\n"))
    frame()
    

word=str(input("Enter the message:""\n"))
repeat=eval(input("Enter the message repeat count:""\n"))
frame=eval(input("Enter the frame thickness:""\n"))
x=2*(frame-1)
space=len(word)
a=space+2
y=0
    
for i in range(frame):
    print("|"*i,end="")
    print("+"+"-"*a,end="")
    print("-"*x+"+",end="")
    print("|"*i)
    x-=2

for j in range(repeat):
    print("|"*frame,word,"|"*frame)

for i in range(frame-1,-1,-1):
    print("|"*i,end="")
    print("+"+"-"*a,end="")
    print("-"*y+"+",end="")
    print("|"*i)
    y+=2
    

word=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
x=2*t
for j in range(t):
        print("|"*j,"+","-"*(len(word)+x),"+","|"*j,sep='')
        x-=2
#print("|+","-"*len(word)+2,"+|",sep='')
for i in range(r):
    print("|"*t,word,"|"*t)
for k in range (t-1,-1,-1):
        print("|"*k,"+","-"*(len(word)+2*(t-k)),"+","|"*k,sep='')
        
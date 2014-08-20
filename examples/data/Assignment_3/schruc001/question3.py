#LineFrame

def frame():        
        message=input("Enter the message:\n")
        rep=eval(input("Enter the message repeat count:\n"))
        t=eval(input("Enter the frame thickness:\n"))
        i=0
        while i in range(0,t):
                print("|"*(i), "+", "-"*(len(message)+2*(t-i)), "+", "|"*(i), sep="")
                i=i+1
        j=0
        while j in range(0,rep):
                print("|"*t, message, "|"*t)
                j=j+1
        k=t-1
        while k in reversed(range(0,t)):
                print("|"*(k), "+", "-"*(len(message)+2*(t-k)), "+", "|"*(k), sep="")
                k=k-1
                
frame()
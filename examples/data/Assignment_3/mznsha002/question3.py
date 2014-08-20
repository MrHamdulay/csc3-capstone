#Drawing a frame around a message
#21 March 2014

def main():        
        message = input("Enter the message:\n")
        repeat = eval(input("Enter the message repeat count:\n"))
        thick = eval(input("Enter the frame thickness:\n"))
        
        i = 0
        while i in range(0,thick):
                print("|"*(i), "+", "-"*(len(message)+2*(thick-i)), "+", "|"*(i), sep="")
                i = i+1
        j = 0
        while j in range(0,repeat):
                print("|"*thick, message, "|"*thick)
                j = j+1
        
        k = thick-1
        while k in reversed(range(0,thick)):
                print("|"*(k), "+", "-"*(len(message)+2*(thick-k)), "+", "|"*(k), sep="")
                k-=1
                
main()
#mr kennedy
def frame():
    m=input("Enter the message:\n")
    w=eval(input("Enter the message repeat count:\n"))
    t=eval(input("Enter the frame thickness:\n"))
    for x in range (0,t):
        print("|"*x+"+"+"-"*(((t-x)*2)+len(m))+"+"+"|"*x)
    
    for p in range(1,w+1):    
            print('|'*t,m,'|'*t)
   
    for y in range (0,t):
        print("|"*(t-y-1)+"+"+"-"*(((y+1)*2)+len(m))+"+"+"|"*(t-y-1))
        

frame()

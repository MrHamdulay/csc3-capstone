def master():
    msg = input("Enter the message:\n")
    cnt = eval(input("Enter the message repeat count:\n"))
    thckss = eval(input("Enter the frame thickness:\n"))
    x = len(msg)
    g = 0
    c = thckss
    s=thckss-1
    while c >= 1:
        print("|"*g+"+"+"-"*x+"-"*(c*2)+"+"+"|"*g)
        c -= 1
        g += 1
        
    for i in range(cnt):
        print("|"*thckss,msg,"|"*thckss)
        
    
    for i in range(thckss):
            x = len(msg)+2*(i+1)
            print("|"*s+"+"+"-"*x+"+"+"|"*s)
            s-=1
        
master()
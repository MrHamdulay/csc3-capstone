def frame():
    msg=input("Enter the message:\n")
    rpt=eval(input("Enter the message repeat count:\n"))
    thk=eval(input("Enter the frame thickness:\n"))
    n=2*thk + rpt
    for i in range(n-1):
        if i ==0 or i == n-1:print("+"+(len(msg)+2+2*thk -4-2*i+2)*"-"+"+")
        elif i <thk:
            print("|"*i+"+"+"-"*(len(msg)+2+2*thk -4-2*i+2)+"+"+"|"*i)
    for i in range(rpt):
        print("|"*thk,msg,"|"*thk)
    for i in range(n,-1,-1):
            if i ==0 :print("+"+(len(msg)+2+2*thk -4-2*i+2)*"-"+"+")
            elif i <thk:
                print("|"*i+"+"+"-"*(len(msg)+2+2*thk -4-2*i+2)+"+"+"|"*i)    
                    
frame()                    
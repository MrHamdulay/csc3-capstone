def Frame():
    #input
    message = input("Enter the message: \n")
    r = eval(input("Enter the message repeat count: \n"))
    frame = eval(input("Enter the frame thickness: \n"))

    #processing -- output
    l = len(message)
    s=""

    for i in range(frame):
        print(s+"+"+"-"*(l+2*frame)+"+"+s)
        s+="|"
        l+=-2
    
    for j in range(r):
    
        print(s+" "+message+" "+s)
        v1=s
        v2=len(s)-1
        l2=len(message)
            
    for k in range(frame):
     
        print(v1[0:v2]+"+"+"-"*(l2+2)+"+"+v1[0:v2])
        l2+=2
        v2+=-1
Frame()    
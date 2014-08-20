def Frame():
    
    message = input("Enter the message: \n")
    
    reap = eval(input("Enter the message repeat count: \n"))

    frameSize = eval(input("Enter the frame thickness: \n"))

 
    leng = len(message)
   
    space=""

    for i in range(frameSize):

        print(space+"+"+"-"*(leng+2*frameSize)+"+"+space)

        space+="|"

        leng-=2
    
    for j in range(reap):
    
        print(space+" "+message+" "+space)

        q1=space

        q2=len(space)-1

        leng2=len(message)
            
    for k in range(frameSize):
     
        print(q1[0:q2]+"+"+"-"*(leng2+2)+"+"+q1[0:q2])

        leng2+=2

        q2+=-1
Frame()    
def frame ():
    msg = input("Enter the message:\n")
    repeat = eval(input("Enter the message repeat count:\n"))
    thick = eval(input("Enter the frame thickness:\n"))
    msgLong = len("|| "+msg+" ||")
    shrink = thick
    #innerFrame
    if repeat >=1:
        
        for y in range(0,thick-1):
            print("|"*y,"+","-"*((len(msg))+((thick-y)*2)),"+","|"*y,sep="")
            shrink = shrink -1
            
        print("|"*(thick-1),"+","-"*(msgLong-4),"+","|"*(thick-1),sep="")
  
        for i in range(repeat):
            print("|"*thick," ",msg," ","|"*thick,sep="")
        
        #print("|"*(thick-1),"+","-"*(msgLong-4),"+","|"*(thick-1),sep="")
        
        for x in range(thick-1,-1,-1):
            print("|"*x,"+","-"*((len(msg))+((thick-x)*2)),"+","|"*x,sep="")
            
    
    

frame()

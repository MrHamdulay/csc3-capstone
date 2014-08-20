def frame():
    M = input("Enter the message:\n") 
    R = int(input("Enter the message repeat count:\n")) #Repeat
    T = int(input("Enter the frame thickness:\n")) #Thickness
    Len = len(M)
    
    for x in range(T):
        print("|"*x + "+" + "-"*((Len)+ 2*(T-x))+ "+" +"|"*x )
    
    
    for x in range(R):
        print("|"*T , M, "|"*T)
    
    for x in range(T-1,-1,-1):
        print("|"*x + "+" + "-"*((Len)+ 2*(T-x))+ "+" +"|"*x )
        

frame()
        
               
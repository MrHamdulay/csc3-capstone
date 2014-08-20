def frame(mes, r, f):
    for t in range(f,0,-1):
        print(("|"*(f-t)), "+-", (len(mes) + (t-1)*2)*"-","-+", ("|"*(f-t)),sep="")
    for i in range(r):
        print("|"*f, mes,"|"*f)
    
    for t in range(1,f+1,1):
        print(("|"*(f-t)), "+-", (len(mes) + (t-1)*2)*"-","-+", ("|"*(f-t)),sep="")
            
m=input("Enter the message:\n")
c=eval(input("Enter the message repeat count:\n"))
w=eval(input("Enter the frame thickness:\n"))
frame(m,c,w)

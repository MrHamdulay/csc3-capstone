def frame():
    mess=input("Enter the message:\n")
    messcount=eval(input("Enter the message repeat count:\n"))
    thick=eval(input("Enter the frame thickness:\n"))
    a=len(mess)
    h=0
    j=thick
    for x in range(thick,0,-1):
        v=("|"*h+"+"+"-"*a+"-"*(thick*2)+"+"+"|"*h)
        print(v)
        h=h+1
        thick = thick-1
  
    for i in range(messcount):
        print("|"*j+" "+mess+" "+"|"*j)
        
    for y in range(thick,0,-1):
        w=("|"*(j-1)+"+"+"-"*(thick/2)+"+"+"|"*(j-1))
        print(w)
            
   
frame()
    
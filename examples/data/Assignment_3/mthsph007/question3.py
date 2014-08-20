#Sphiwe Muthembi
#mthsph007

#frames

def frames(msg,loop,fthick):
    #defining values
   # mlen= len("|| "+msg+" ||")
    mlen= len("|"*fthick+" "+msg+" "+fthick*"|") - 2
    
    #frame
    border= 0
    for border in range(fthick):
        minus= mlen-(border*2)
        print("|"*border + "+" + "-"*minus + "+" + border*"|")
    i= 1
    r=1
    while i <= loop:
       # loopmsg= ("||  "+msg+"  ||")*r
        loopmsg= ("|"*fthick+" "+msg+" "+fthick*"|")*r
        print(loopmsg)
        i+=1
    minus= mlen+(border*2)
    for border in range(fthick-1,-1,-1):
        minus= mlen-(border*2)
        print("|"*border + "+" + "-"*minus +"+" + border*"|")
        
output= input("Enter the message:\n")
looper= eval( input("Enter the message repeat count:\n"))
thickness= eval( input("Enter the frame thickness:\n"))
frames(output,looper,thickness)        
        
    
    #Done
    
    
    
    
    
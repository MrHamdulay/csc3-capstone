
#message.. frame

ms=input(("Enter the message:\n"))
mrep=eval(input("Enter the message repeat count:\n"))
Frth=eval(input("Enter the frame thickness:\n"))
Frth2=Frth
line=0
line2=Frth
while Frth > 0:
    print("|"*line+"+"+("-"*len(ms))+"-"*((Frth-1)*2)+"--"+"+"+"|"*line)
    Frth-=1
    line+=1
while mrep>0:
    print(("|"*(Frth2)+" "+ms+" "+"|"*(Frth2)))
    mrep-=1
dash=0
while Frth2 > 0:
    print((line2-1)*"|"+"+"+(len(ms)*"-")+("-"*dash)+"--"+"+"+(line2-1)*"|")
    dash+=2
    Frth2-=1
    line2-=1
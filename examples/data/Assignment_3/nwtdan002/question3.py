print("Enter the message:")
mes=input()
print("Enter the message repeat count:")
mrep=eval(input())
print("Enter the frame thickness:")
Frth=eval(input())
Frth2=0
Frth2=Frth
line=0
line2=Frth
while Frth > 0:
    print("|"*line+"+"+("-"*len(mes))+"-"*((Frth-1)*2)+"--"+"+"+"|"*line)
    Frth-=1
    line+=1
while mrep>0:
    print(("|"*(Frth2)+" "+mes+" "+"|"*(Frth2)))
    mrep-=1
dash=0
while Frth2 > 0:
    print((line2-1)*"|"+"+"+(len(mes)*"-")+("-"*dash)+"--"+"+"+(line2-1)*"|")
    dash+=2
    Frth2-=1
    line2-=1
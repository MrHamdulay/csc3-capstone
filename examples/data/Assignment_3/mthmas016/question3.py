txt=input("Enter the message:\n")
rpt=int(input("Enter the message repeat count:\n"))
thk=int(input("Enter the frame thickness:\n"))
width=len(txt)+2+(thk*2)
def frame():
    for i in range (0,thk):
        print(("|"*i)+"+"+((width-(2*(i+1)))*"-")+"+"+("|"*i))
    for j in range(0,rpt):
        print(("|"*thk)+" "+txt+" "+("|"*thk))
def bottom(thk):
    for k in range(thk):
        print("|"*(thk-k-1)+"+"+"-"*(2*k+2+len(txt))+"+"+"|"*(thk-k-1))
frame()
bottom(thk)

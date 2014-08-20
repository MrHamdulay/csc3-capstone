msg=input("Enter the message: \n")
rpt=eval(input("Enter the message repeat count: \n"))
tkns=eval(input("Enter the frame thickness: \n"))
frmx=0
x=len(msg)+tkns
for i in range(tkns):
    print(frmx*"|","+",(x+tkns)*"-","+",frmx*"|",sep="")
    frmx+=1
    x-=2
for a in range(rpt):
    print(tkns*"|",msg,tkns*"|",sep=" ")
frmx=tkns-1
x=len(msg)+2
for b in range(tkns):
    print(frmx*"|","+",x*"-","+",frmx*"|",sep="")
    frmx-=1
    x+=2    
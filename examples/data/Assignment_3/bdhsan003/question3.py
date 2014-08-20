#STUDENT NO:BDHSAN003
def Box():
    msg=input("Enter the message: \n")
    repeat=int(input("Enter the message repeat count: \n"))
    thickness=int(input("Enter the frame thickness: \n"))
    lngt=len(msg)
    empty=""

    for i in range(thickness):
        print(empty+"+"+"-"*(lngt+2*thickness)+"+"+empty)
        empty=empty+"|"
        lngt=lngt-2
    
    for j in range(repeat):
        print(empty+" "+msg+" "+empty)
        a=empty
        a2=len(empty)-1
        lngt2=len(msg)
            
    for k in range(thickness):
        print(a[0:a2]+'+'+'-'*(lngt2+2)+"+"+a[0:a2])
        lngt2=lngt2+2
        a2=a2-1
Box()    
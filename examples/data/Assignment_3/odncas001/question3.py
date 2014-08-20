def frame(phr,rep,thck):
    strlen=len(phr)+2
    for i in range(thck):
        hyph=(strlen+2*(thck-1))-2*i
        print(i*"|","+","-"*hyph,"+",i*"|",sep="")
    for i in range(rep):
        print(thck*"|",phr,thck*"|",sep=" ")
    for i in range(thck):
        hyph=(strlen)+2*i
        line=thck-(i+1)
        print(line*"|","+",hyph*"-","+",line*"|",sep="")

phr=input("Enter the message:\n")
rep=eval(input("Enter the message repeat count:\n"))
thck=eval(input("Enter the frame thickness:\n"))
frame(phr,rep,thck)
         
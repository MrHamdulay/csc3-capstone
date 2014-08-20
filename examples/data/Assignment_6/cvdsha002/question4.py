#shahrain Coovadia
def list():
    l=input("Enter a space-separated list of marks:\n")       #input
    l=l.split(" ")
    
    return l
    
def histogram ():
    l=list()
    v=0
    w=0                #assign variables
    x=0
    y=0
    z=0
    for i in l:
        i=eval(i)
        if i<50:                      #mark allocations
            v=v+1
        elif 50<=i<60:
            w=w+1
        elif 60<=i<70:
            x=x+1
        elif 70<=i<75:
            y=y+1
        elif i>=75:
            z=z+1
    print("1 ", "|", "X"*z, sep="")                    #display of histogram
    print("2+", "|", "X"*y, sep="")
    print("2-", "|", "X"*x, sep="")
    print("3 ", "|", "X"*w, sep="")
    print("F ", "|", "X"*v, sep="")
     
histogram()
 
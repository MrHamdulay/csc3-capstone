#Azhar Aboobaker
#ABBAZH001
#23/04/2014

def marks():
    x=input("Enter a space-separated list of marks:\n")
    x=x.split(" ")
    y=[]
    for i in x:
        y.append(eval(i))
    return y

def histogramrepresentation():
    x=marks()
    a,b,c,d,e=0,0,0,0,0
    for i in x:
        if i<50:
            a=a+1
        elif 50<=i<60:
            b=b+1
        elif 60<=i<70:
            c=c+1
        elif 70<=i<75:
            d=d+1
        elif i>=75:
            e=e+1
    print("1 ", "|", "X"*e, sep="")
    print("2+", "|", "X"*d, sep="")
    print("2-", "|", "X"*c, sep="")
    print("3 ", "|", "X"*b, sep="")
    print("F ", "|", "X"*a, sep="")
    
histogramrepresentation()
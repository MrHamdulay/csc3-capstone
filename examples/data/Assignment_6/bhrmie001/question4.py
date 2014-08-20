def getmarks():
    x=input("Enter a space-separated list of marks:\n")
    x=x.split(" ")
    y=[]
    for i in x:
        y.append(eval(i))
    return y

def histogram():
    x=getmarks()
    a=0
    b=0
    c=0
    d=0    #variables to count the amount of occurances
    e=0
    for i in x:
        if i<50:
            a+=1
        elif 50<=i<60:
            b+=1
        elif 60<=i<70:
            c+=1
        elif 70<=i<75:
            d+=1
        elif i>=75:
            e+=1
    print("1 ", "|", "X"*e, sep="")
    print("2+", "|", "X"*d, sep="")
    print("2-", "|", "X"*c, sep="")
    print("3 ", "|", "X"*b, sep="")
    print("F ", "|", "X"*a, sep="")
    
histogram()
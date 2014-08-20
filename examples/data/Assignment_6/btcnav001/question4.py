def main():
    x=input("Enter a space-separated list of marks:\n")
    
    y=x.split(' ')
    fail=0
    third=0
    lower_2=0
    upper_2=0
    first=0
    z=(len(y))
    a=0
    for i in range(z):
        a=eval((y[i]))

        if a>=0 and a<50:
            fail=fail+1
        elif a>=0 and a<60:
            third=third+1
        elif a>=60 and a<70:
            lower_2=lower_2+1
        elif a>=70 and a<75:
            upper_2=upper_2+1
        else:
            first=first+1
    print("1 |",first*"X",sep="")
    print("2+|",upper_2*"X",sep="")
    print("2-|",lower_2*"X",sep="")
    print("3 |",third*"X",sep="")
    print("F |",fail*"X",sep="")
main()
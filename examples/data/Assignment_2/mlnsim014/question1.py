def smanga():
    year=eval(input("Enter a year:\n"))
    p = year%400
    c = year%4
    u = year%100
    if p==0 or c==0 and u!=0:
        print("",year," is a leap year.",sep="")
    else:
        print("",year," is not a leap year.", sep="")
smanga()
    
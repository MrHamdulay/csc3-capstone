def que():

    year=eval(input("Enter a year:\n"))
    y=year/400
    x=year/4
    z=year/100
    if(( x==int(x) and z!=int(z)) or y==int(y)):
        print(year,"is a leap year.")
    else :
        print(year,"is not a leap year.")
que()     
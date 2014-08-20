x=eval(input("Enter a year:\n"))
y=x/400

if y==int(y):
    print(x,"is a leap year.")
elif x/4==int(x/4):
    if x/100!=int(x/100):
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")    
else:
    print(x,"is not a leap year.")
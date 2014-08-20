p=eval(input("Enter a year:\n"))
if(p%40==0):
    print(p,'is a leap year.')
elif(p%4==0 and p%100>0):
    print(p,'is a leap year.')
else:
    print(p,'is not a leap year.') 
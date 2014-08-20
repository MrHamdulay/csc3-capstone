gh=eval(input("Enter a year:\n"))
if(gh%40==0):
    print(gh,'is a leap year.')
elif(gh%4==0 and gh%100>0):
    print(gh,'is a leap year.')
else:
    print(gh,'is not a leap year.') 
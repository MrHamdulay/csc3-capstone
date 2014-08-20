#Phillip Ruhesi
x=eval(input('Enter a year:\n')) #prompts the user to type in a year
rem=x%400                        #calculates a remainder when x is divided by 400
rem2=x%4                         #calculates a remainder when x is divided by 4
rem3=x%100                       #calculates a remainder when x id divided by 100
if rem == 0 :
    print(x,'is a leap year.')
elif rem2==0 and rem3!=0:
    print(x,'is a leap year.')
else:
    print(x,'is not a leap year.')
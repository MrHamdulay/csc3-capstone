#question1.py
#Created by Sibabalwe Qamata
x=eval(input("Enter a year:\n"))
if(x%40==0):
    print(x,'is a leap year.')
elif(x%4==0 and x%100>0):
    print(x,'is a leap year.')
else:
    print(x,'is not a leap year.') 
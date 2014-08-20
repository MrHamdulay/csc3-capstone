#Leap year or not
#Mahnoor Ahmed
#AHMMAH001

y=input("Enter a year:\n")
y=eval(y)
if (y%400==0) or (y%4==0 and y%100>0):
    print(y,"is a leap year.") 
else:
    print(y,"is not a leap year.")
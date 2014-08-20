year=eval(input("Enter a year:\n"))
answer1=year%400
answer2=year%4
answer3=year%100
if answer1 is 0 or answer2 is 0 and answer3 is not 0 :
    print(year,"is a leap year.")
else :
    print(year,"is not a leap year.")
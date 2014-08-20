leap = "false"
year=eval(input("Enter a year:\n"))

if ( year%400 == 0 ):
    leap = "true"
elif (( year%4 == 0 ) and ( year%100 != 0 )) : 
    leap = "true"
if leap == "true" :
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")

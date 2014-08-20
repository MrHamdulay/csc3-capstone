year = eval (input ("Enter a year:\n") )
if year // 400 * 400 == year / 400 * 400 :
    print (year, "is a leap year.")
elif year // 100 * 100 == year / 100 * 100 :
    print (year, "is not a leap year.")
elif year // 4 * 4 == year / 4 * 4:
    print (year, "is a leap year.")
else :
    print (year, "is not a leap year.")
yr = eval(input("Enter a year: \n"))
if (yr%400 == 0):
    print (yr , "is a leap year.")
elif(yr%4==0) and (yr%100 != 0):
    print (yr , "is a leap year.")
    
else:
        print (yr , "is not a leap year.")



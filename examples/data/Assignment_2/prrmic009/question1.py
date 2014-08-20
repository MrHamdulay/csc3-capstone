# program to check if a year is a leap year or not
# Mick Perring
# 8 March 2014

# lets user input a year
year = eval(input("Enter a year:""\n"))

if (year % 4) == 0:                              # checks if year is divisible by 4
    if (year % 100) == 0:                        # checks if year is divisible by 100
        if (year % 400) == 0:                    # checks if year is divisible by 400
            print (year,"is a leap year.")       # if all are true, prints result (leap year)
        else:                                    # if divisible by 4 & 100, but not 400, prints result (not leap year)
            print (year,"is not a leap year.")
    else:                                        # if divisible by 4, but not 100, prints result (leap year)
        print (year,"is a leap year.")
else:                                            # if not divisible by 4, prints result (not leap year)
    print (year,"is not a leap year.")

            


# question1
# a program to determine whether a year is a leap year or not
# Thomas Konigkramer
# 8 March 2014

# asking for input from user
year = eval(input("Enter a year:\n"))

# processing inputted information: 
if year/4 == year//4 and year/100 != year//100:
    print(year, "is a leap year.")

elif year/400 == year//400:
    print(year, "is a leap year.")
    
else:
    print(year, "is not a leap year.")
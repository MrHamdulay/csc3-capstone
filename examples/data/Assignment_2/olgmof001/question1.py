# a program saying whether years are leap years or not
# Tofunmi Olagoke
# 13 March 2014
# OLGMOF001


ques=eval(input("Enter a year:\n"))
if ques%400==0 or ques%4==0 and not ques%100==0:
    print(ques,"is a leap year.")
else:
    print(ques,"is not a leap year.")
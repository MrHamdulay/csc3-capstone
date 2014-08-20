# Luke Henkeman
# HNKLUK001
# Assignment 2, Question 1, CSC1015F
# 7 March 2014

def leapyear():
    input_year = eval(input("Enter a year:\n"))
    leap400int = input_year // 400
    leap400nml = input_year / 400
    leap4int = input_year // 4
    leap4nml = input_year / 4
    leap100int = input_year // 100
    leap100nml = input_year / 100
    if(leap400int == leap400nml):
        print(input_year,"is a leap year.")
    elif(leap4int == leap4nml):
        if(leap100int != leap100nml):
            print(input_year,"is a leap year.")
        else:
            print(input_year,"is not a leap year.")
    else:
        print(input_year,"is not a leap year.")

leapyear()
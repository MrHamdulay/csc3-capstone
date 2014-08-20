# Assignment 1: Question 2
# Write a program to check the validity of a time entered by the user as a set of three integers
# Author: Barnett Msiska(MSSBAR002)
# Date: 25/02/2014

def main():
    # requeust user input
    hours = eval(input("Enter the hours: \n"))
    minutes = eval(input("Enter the minutes: \n"))
    seconds = eval(input("Enter the seconds: \n"))
    
    # check user input
    if not(0 <= hours < 24):
        print("Your time is invalid.")
    elif not(0 <= minutes < 60) or not(0 <= seconds < 60):
        print("Your time is invalid.")
    else:
        print("Your time is valid.")

main()
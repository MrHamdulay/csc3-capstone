# Assignment 1
# Carl-David Sandile Saldanha
# SLDCAR001
# February 2014
# Question 2
def time():
    h=eval(input("Enter the hours:\n"))
    m=eval(input("Enter the minutes:\n"))
    s=eval(input("Enter the seconds:\n"))
    if 0<=h and h<=23 and 0<=m and m<=59 and 0<=s and s<=59:
            print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
time()
        
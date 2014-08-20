#ASSIGNMENT 2 QUESTION 1
#STUDENT NO.: NDXSHE013

def main():
    year=eval(input("Enter a year:\n"))
    ans2=year/4
    ans1=year/400
    ans3=year/100
    if ans1 == int(ans1):
        print(year,"is a leap year.")
    elif ans2 == int(ans2) and  ans3 !=int(ans3):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
main()
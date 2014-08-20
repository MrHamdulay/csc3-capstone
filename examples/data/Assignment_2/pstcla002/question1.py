# Assignment 2 question 1
# leap year
def main():
    x=eval(input("Enter a year:\n"))
    if x/400 == x//400:
        print(x,"is a leap year.")
    elif x/4 == x//4 and x/100!=x//100:
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")
main()
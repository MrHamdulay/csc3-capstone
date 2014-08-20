def isLeap(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

if __name__ == "__main__":
    print("Enter a year:")
    year = eval(input())
    if isLeap(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

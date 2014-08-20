def main():
    year=eval(input("Enter a year:\n"))
    answer1=year/400
    answer2=year/4
    answer3=year/100
    if answer1 == int(answer1):
        print(year,"is a leap year.")
    elif answer2 == int(answer2) and  answer3 !=int(answer3):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
main()
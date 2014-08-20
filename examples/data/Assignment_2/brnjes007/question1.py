def leapyear():
    a=(eval(input("please enter a year:")))

    if a % 4==0 or a % 400==0:
        print("This is a leap year\n")
    else:
        print("This is not a leap year\n")

if __name__=='__main__':
    leapyear()
            
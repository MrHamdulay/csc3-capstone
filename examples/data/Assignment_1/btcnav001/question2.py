def main():
    x=eval(input("Enter the hours:\n"))
    y=eval(input("Enter the minutes:\n"))
    z=eval(input("Enter the seconds:\n"))
    if x>24 or x<0:
        print("Your time is invalid.")
    elif y>60 or y<0:
        print("Your time is invalid.")
    elif z>60 or z<0:
        print("Your time is invalid.")
    else:
        print("Your time is valid.")
main()
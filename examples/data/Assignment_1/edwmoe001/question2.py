def main():
    x=eval(input("Enter the hours:\n"))
    y=eval(input("Enter the minutes: \n"))
    z=eval(input("Enter the seconds: \n"))
    if x<0:
        print("Your time is invalid.")
    elif x>23:
        print("Your time is invalid.")
    elif y<0:
        print("Your time is invalid.")
    elif y>59:
        print("Your time is invalid.")
    elif z<0:
        print("Your time is invalid.")
    elif z>59:
        print("Your time is invalid.")
    else:
        print("Your time is valid.")
           
main()
def main():
    x=eval(input("Enter the hours:\n"))
    y=eval(input("Enter the minutes:\n"))
    z=eval(input("Enter the seconds:\n"))
    if (0<=x<=23) and (0<=y<=59) and (0<=z<=59):
        print("Your time is valid.\n")
    else:
        print("Your time is invalid.\n")
          
main() 
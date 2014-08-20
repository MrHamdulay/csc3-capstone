def main():
    x=eval(input("Enter the hours:\n"))
    y=eval(input("Enter the minutes:\n"))
    z=eval(input("Enter the seconds:\n"))
    if type(x)==int and 0<=x<=23 and type(y)==int and 0<=y<=59 and type(z)==int and 0<=z<=59:
        print("Your time is valid.")
    else: 
        print("Your time is invalid.")
main()
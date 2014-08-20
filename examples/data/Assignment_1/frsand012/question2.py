# Valid Time
# Andrew Forson

def time():
    a=eval(input("Enter the hours:\n"))
    b=eval(input("Enter the minutes:\n"))
    c=eval(input("Enter the seconds:\n"))
    if 0<=a<=23 and 0<=b<=59 and 0<=c<=59:
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
time()

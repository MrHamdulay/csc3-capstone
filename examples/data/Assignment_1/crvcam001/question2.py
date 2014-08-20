# program to check the validity of a time entered by the user as a set of three integers
# camilla craven
# 28 February 2014

def main():
    hours=eval(input("Enter the hours:\n")) # user inputs hours
    minutes=eval(input("Enter the minutes:\n")) # user inputs minutes
    seconds=eval(input("Enter the seconds:\n")) # user inputs seconds
    
    if hours<=23 and hours>=0 and minutes<=59 and minutes>=0 and seconds<=59 and seconds>=0: # setting limits
        print("Your time is valid.")
    else: print("Your time is invalid.")    

main()
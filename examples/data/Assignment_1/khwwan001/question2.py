def main():
    
# This program prompts the user to enter his/her time in hours, minutes and seconds and then it checks for the validity of the values that he/she entered.
    hours = eval(input("Enter the hours:\n"))
    minutes = eval(input("Enter the minutes:\n"))
    seconds = eval(input("Enter the seconds:\n"))
    if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59 :
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
main()
        
    
    
    
    
    
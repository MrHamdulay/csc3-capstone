# Author : Rayaan Fakier FKRRAY001
# Date : 28 - 02 - 2014

# Main function to take input of time and output validity
def main():
    # inputs for time
    get_Hours = int(input("Enter the hours: \n"))
    get_Minutes = int(input("Enter the minutes: \n"))
    get_Seconds = int(input("Enter the seconds: \n"))
    
    # if statement to check validity of time input
    if (get_Hours > 23 or get_Hours < 0) or (get_Minutes > 59 or get_Minutes < 0) or (get_Seconds > 59 or get_Seconds < 0): 
        print("Your time is invalid.")
    else: 
        print("Your time is valid.")

# call main function
main()
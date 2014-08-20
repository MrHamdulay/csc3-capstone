# A program to check the validity of time entered by a user (as a set of three integers)
# Afika Nyati
# 25 February 2014

def main():
    try:
        hours = eval(input("Enter the hours:\n"))
        minutes = eval(input("Enter the minutes:\n"))
        seconds = eval(input("Enter the seconds:\n"))
    
    
        if (0<= hours <=23 and 0<= minutes <=59 and 0<= seconds <=59):
            print("Your time is valid.")
    
        else:
            print("Your time is invalid.") 
    
    except NameError:
        print("Your time is invalid.")
        
main()
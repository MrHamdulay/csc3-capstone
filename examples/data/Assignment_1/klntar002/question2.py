# program to check the validity of a time entered by a user
# tarisai stephen kalinde
# klntar002

def main():
    hrs= eval(input("Enter the hours: \n"))
    mins= eval(input("Enter the minutes: \n"))
    sec= eval(input("Enter the seconds: \n"))
    if (0<=hrs<24) and (0<=mins<60) and (0<=sec<60) :
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
main()        
    
    

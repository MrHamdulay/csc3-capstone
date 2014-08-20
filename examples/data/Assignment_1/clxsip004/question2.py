#Siphesihle Cele
#assignment 1 
#Question 2
#26 february 2014


hours=eval(input("Enter the hours:\n"))

minutes=eval(input("Enter the minutes:\n"))

seconds=eval(input("Enter the seconds:\n"))

if hours>=0 and hours<=23:

    if minutes>=0 and minutes<=59:
   
        if seconds>=0 and seconds<=59:
            print("Your time is valid.")
        elif seconds > 59 or seconds<0:
            print("Your time is invalid.")
            
    elif minutes > 59 or minutes<0:
        print("Your time is invalid.")    
else:
    print("Your time is invalid.")


    

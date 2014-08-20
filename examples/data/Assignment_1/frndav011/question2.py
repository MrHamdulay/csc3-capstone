#Assignment 1
# Question 2

# User input and output

h = eval(input("Enter the hours:\n"))

m = eval(input("Enter the minutes:\n"))

s = eval(input("Enter the seconds:\n"))


# If else satement to determine validity of time inputs

if (h<0) or (h>23): # Hours range
    print("Your time is invalid.")
elif (m<0) or (m>59):# Minutes range
    print("Your time is invalid.")
elif (s<0) or (s>59) : # Seconds range
    print("Your time is invalid.")
    
else:
    print("Your time is valid.")



    

    
    

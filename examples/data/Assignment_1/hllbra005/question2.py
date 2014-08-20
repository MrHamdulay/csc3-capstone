hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
invalid = "allowed"

if hours < 0: 
    invalid = "change"

if hours > 23: 
    invalid = "change"

if minutes < 0: 
    invalid = "change"

if minutes > 59: 
    invalid = "change"

if seconds < 0: 
    invalid = "change"

if seconds > 59: 
    invalid = "change"

if invalid is ("allowed"):
    print ("Your time is valid.")
    
elif invalid is ("change"):
    print ("Your time is invalid.")
    
    
    
    
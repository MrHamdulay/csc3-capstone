
def timing():
    
    kangaroo= eval(input("Enter the hours: \n"))
    penguin= eval(input("Enter the minutes: \n"))
    rocket= eval(input("Enter the seconds: \n"))
    
    if (kangaroo<0 or kangaroo>23):
        print ("Your time is invalid.")
    elif(penguin<0 or penguin>59):
        print ("Your time is invalid.")
    elif(rocket<0 or rocket>59):
            print ("Your time is invalid.")
    else:
        print ("Your time is valid.")    
        
timing()
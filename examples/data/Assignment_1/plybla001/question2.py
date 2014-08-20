#Validate
#B.PLAYER
#27/02/2014

def validate():
    hours= eval(input("Enter the hours:\n"))
    mins = eval(input("Enter the minutes:\n"))
    sec= eval(input("Enter the seconds:\n"))    
    if(hours>23 or hours<0):
        print("Your time is invalid.")
    elif(mins<0 or mins>59):
        print("Your time is invalid.")
    elif(sec<0 or sec>59):
        print("Your time is invalid.")
    else:
        print("Your time is valid.")
        
def main():   
    validate()
    
main()
    
    
        

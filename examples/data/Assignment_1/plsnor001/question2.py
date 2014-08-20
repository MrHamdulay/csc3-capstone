
def intake():
    hours=int(input('Enter the hours:\n'))
    minutes=int(input('Enter the minutes:\n'))
    seconds=int(input('Enter the seconds:\n'))
    
    def checks():
    
        if hours in range(0,24) and minutes in range(60) and seconds in range(60):
            print('Your time is valid.')
        else:
            print('Your time is invalid.')
         
    checks()
        
intake()
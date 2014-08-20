# Program to check validity of user-entered time
# Irfan Habib
# 2 March 2014

def ValidateTime() :
    hours = eval(input('Enter the hours:\n'))
    minutes = eval(input('Enter the minutes:\n'))
    seconds = eval(input('Enter the seconds:\n'))
    if 23 >= hours >=0 and 59 >= minutes >= 0 and 59 >= seconds >= 0:
        print('Your time is valid.')
    else: print('Your time is invalid.')
    
ValidateTime()      
    
        
        
        
    

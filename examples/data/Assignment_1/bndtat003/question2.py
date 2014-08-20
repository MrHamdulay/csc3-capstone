# Program to check the validity of the time entered

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 04-02-2014


a = eval(input('Enter the hours:\n'))

b = eval(input('Enter the minutes:\n'))

c = eval(input('Enter the seconds:\n'))


if a<0 or b<0 or c<0:
    print('Your time is invalid.')
    
elif a>24 or b>= 60 or c >= 60:
    print('Your time is invalid.')
    
else:
    print('Your time is valid.')
        
        

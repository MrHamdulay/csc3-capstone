#program to check the validity of a user's time value input
#Luke Naude
#1 march 2014

#function to check the users values
def check_value():
    if 0<=x<=23 and 0<=y<=59 and 0<=z<=59:
        print('Your time is valid.')
    else:
        print('Your time is invalid.')
    


print('Enter the hours:')   #gives user a command
x=eval(input())                   #stores value
print('Enter the minutes:')  
y=eval(input())
print('Enter the seconds:')
z=eval(input())
check_value()


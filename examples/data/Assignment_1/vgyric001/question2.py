# Question 2
def time():
    hours = eval(input('Enter the hours:'+ '\n'))
    minutes = eval(input('Enter the minutes:'+ '\n'))
    seconds = eval(input('Enter the seconds:'+ '\n'))
    
    if(hours>23 or hours<0) or (minutes>60 or minutes<0) or (seconds>60 or seconds<0):
        print("Your time is invalid.")
    else:
        print("Your time is valid.")
time()
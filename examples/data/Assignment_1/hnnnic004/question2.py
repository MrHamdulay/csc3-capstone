#hnnnic004
#assignment 1
#question 2
#due: 7/03/14

#ask for the time
#say whether time is valid/invalid

def time (hours, minutes, seconds):
    if 0<=hours<=23 and 0<=minutes<=60 and 0<=seconds<=60:
        print("Your time is valid.")
    else: 
        print("Your time is invalid.")
        
def main ():
    hours = eval(input("Enter the hours:\n")) 
    minutes = eval(input("Enter the minutes:\n"))
    seconds = eval(input("Enter the seconds:\n"))
    time (hours,minutes,seconds)

main()
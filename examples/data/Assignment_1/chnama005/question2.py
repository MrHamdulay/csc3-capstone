# amanda chonco
# time validity
# 5 march 2014

print("Enter the hours:")
hours=eval(input())
print("Enter the minutes:")
minutes=eval(input())
print("Enter the seconds:")
seconds=eval(input())

def time():
    if hours<0 or hours>23 and 0<=minutes<=59 and 0<=seconds<=59:
       print("Your time is invalid.")
    elif minutes<0 or minutes>59 and 0<=hours<=23 and 0<=seconds<=59:
       print("Your time is invalid.")
    elif seconds<0 or seconds>59 and 0<=hours<=23 and 0<=minutes<=59:
       print("Your time is invalid.")
    else:
        print("Your time is valid.")
        
time()
    

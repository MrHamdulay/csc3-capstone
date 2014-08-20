h=int(input("Enter the hours: \n")) 
m=int(input("Enter the minutes: \n"))
s=int(input("Enter the seconds: \n"))
def time():
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        print ("Your time is valid.")
    else:
        print("Your time is invalid.")
        
time()
    
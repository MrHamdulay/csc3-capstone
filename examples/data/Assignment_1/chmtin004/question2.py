#Program to varify time
#Tinotenda Chemvura (CHMTIN004)
#26 February 2014

#_________________Program Starts Here__________________**
def time():
    h=eval(input("Enter the hours:\n"))
    m=eval(input("Enter the minutes:\n"))
    s=eval(input("Enter the seconds:\n"))
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
    
time()

#_________________Program Ends Here____________________**
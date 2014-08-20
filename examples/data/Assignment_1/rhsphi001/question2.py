# phillip ruhesi
# program to check the validity of time
x=eval(input("Enter the hours:\n"))     #Prompts the users to enter the number of hours
y= eval(input("Enter the minutes:\n"))  #Prompts the users to enter the number of minutes
z= eval(input("Enter the seconds:\n"))  #Prompts the users to enter the number of seconds
if 0<=x<=23 and 0<=y<=59 and 0<=z<=59:
    print('Your time is valid.')
else:
    print('Your time is invalid.')
                              
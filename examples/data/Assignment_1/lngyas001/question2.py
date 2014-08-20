#program to check validity of time entered
hours = eval(input('Enter the hours:'))
minutes = eval(input('\nEnter the minutes:'))
seconds = eval(input('\nEnter the seconds:'))
#check validity 
if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("\nYour time is valid.")

else: print('\nYour time is invalid.')
    
  
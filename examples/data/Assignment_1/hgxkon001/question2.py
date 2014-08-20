h = eval(input("Enter the hours:"'\n'))

m = eval(input("Enter the minutes:"'\n'))

s = eval(input("Enter the seconds:"'\n'))

if h>23 or h<0 or m>59  or m<0 or s>59 or s<0:
    print('Your time is invalid.')
else:
    print("Your time is valid.")
    


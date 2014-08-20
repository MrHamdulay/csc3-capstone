a=eval(input("Enter the hours:"))
b=eval(input("Enter the minutes:"))
c=eval(input("Enter the seconds:"))
if a<0 or a>23 or b<0 or b>59 or c<0 or c>59:
    print("Your time is invalid.")
else:
    print("Your time is valid.")
       
     
#program to check a time's validity
#Name: Ailsa Mackay
#Date: 2014-02-26
h=eval(input("Enter the hours:"))
print("")
m=eval(input("Enter the minutes:"))
print("")
s=eval(input("Enter the seconds:"))
print("")
   
if h<0 or h>23 or m<0 or m>59 or s<0 or s>59:
    print("Your time is invalid.")
else:
    print("Your time is valid.")

    
#Question 2
#Name: Liam Brodie
#Student Number: BRDLIA004
#Date: 26 Feb.2014

Hours= input("Enter the hours:\n")
Hours=eval(Hours)
Minutes= input("Enter the minutes:\n")
Minutes=eval(Minutes)
Seconds= input("Enter the seconds:\n")
Seconds=eval(Seconds)

if Hours>23 or Hours<0:
    print("Your time is invalid.")  
elif Minutes>60 or Minutes<0:
        print("Your time is invalid.")
elif Seconds>60 or Seconds<0:
            print("Your time is invalid.")
else:
    print("Your time is valid.")
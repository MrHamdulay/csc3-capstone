# Ayesha Semaar
# Check validity of time
#26 Feb 2014
Hours= input("Enter the hours:\n")
Minutes= input ("Enter the minutes:\n")
Seconds= input ("Enter the seconds:\n")
Hours=eval(Hours)
Minutes=eval(Minutes)
Seconds=eval(Seconds)
if(0 <= Hours <= 23 and 0<= Minutes <= 59 and 0 <= Seconds <= 59 and type(Minutes)==int and type(Hours)==int and type(Seconds)==int):
    print("Your time is valid.") 
else: 
    print("Your time is invalid.")


   

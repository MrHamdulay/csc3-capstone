#Dumisani Ngwenza
#26 February 2014
#NGWDUM005
#Program to check if time entered by a user is valid

Hours = eval(input ("Enter the hours:\n"))
Minutes = eval(input ("Enter the minutes:\n"))
Seconds = eval(input ("Enter the seconds:\n"))

if Hours >=0 and Hours <=23 and Minutes >= 0 and Minutes <=59 and Seconds >=0 and Seconds <= 59: #checks if condition is met
    print ("Your time is valid.")
else:
    print ("Your time is invalid.")
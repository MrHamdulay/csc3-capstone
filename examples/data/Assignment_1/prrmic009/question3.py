# program to generate a personalised spam message based on the user's full name, country and a sum of money
# Mick Perring
# 27 February 2014

first_name= input("Enter first name:""\n")             # allows user to enter first name
last_name= input("Enter last name:""\n")               # allows user to enter last name
money= eval(input("Enter sum of money in USD:""\n"))   # allows user to enter a sum of money
country= input("Enter country name:""\n")              # allows user to enter country

# text to be printed with input variables throughout 
print ("\n""Dearest ",first_name, sep='')
print ("It is with a heavy heart that I inform you of the death of my father,")
print ("General Fayk ",last_name,", your long lost relative from Mapsfostol.", sep='')
print ("My father left the sum of ",money,"USD for us, your distant cousins.", sep='')
print ("Unfortunately, we cannot access the money as it is in a bank in ",country,".", sep='')
print ("I desperately need your assistance to access this money.")
print ("I will even pay you generously, 30% of the amount - ",money*0.3,"USD,", sep='')
print ("for your help.  Please get in touch with me at this email address asap.")
print ("Yours sincerely")
print ("Frank ",last_name, sep='')
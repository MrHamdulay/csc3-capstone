#Aiden Walton
#WLTAID001
#Program to print personalised spam message

firstName = input("Enter first name:\n") #ask user for first name
lastName = input("Enter last name:\n") #ask user for last name
money = eval(input("Enter sum of money in USD:\n")) #ask user for money sum
money30 = 0.3*money #calculate 30% value
country = input("Enter country name:\n") #ask user for country name

#print spam message
print ()
print ("Dearest", firstName, end="\n")
print ("It is with a heavy heart that I inform you of the death of my father,",end="\n")
print ("General Fayk ",lastName,", your long lost relative from Mapsfostol.",end="\n", sep="")
print ("My father left the sum of ",money,"USD for us, your distant cousins.",end="\n",sep="")
print ("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep='',end="\n")
print ("I desperately need your assistance to access this money.")
print ("I will even pay you generously, 30% of the amount - ",money30,"USD,",end="\n",sep="")
print ("for your help.  Please get in touch with me at this email address asap.",end="\n")
print ("Yours sincerely",end="\n")
print ("Frank",lastName)
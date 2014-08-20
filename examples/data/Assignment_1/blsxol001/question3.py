# a program to generate a  personalised spam message
# Xola Bilose
# 26/02/2014

# naming variables to store information given by user
first_name = input("Enter first name:\n") # promting user to enter first name 
last_name = input("Enter last name:\n") # asks for last name
money = eval(input("Enter sum of money in USD:\n")) 
money30 = money*0.3
country = input("Enter country name:\n")
print("Dearest", first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ",last_name,", your long lost relative from Mapsfostol.",sep = '')
print("My father left the sum of ",money,"USD for us, your distant cousins.",sep='')
print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep='')
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",money30,"USD,",sep='')
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",last_name)
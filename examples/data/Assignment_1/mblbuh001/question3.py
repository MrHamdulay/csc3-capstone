# Program to generate a personalised spam message
# Name: Buhlebezwe Mbele
# Student Number: MBLBUH001
# Date: 03 March 2014

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
moneyUSD = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

print(end='\n')
print("Dearest",first_name)
print("It is with a heavy heart that I inform you of the death of my father,",end='\n')
print("General Fayk",last_name,end=',')
print(" your long lost relative from Mapsfostol.",end='\n')
print("My father left the sum of",moneyUSD,end='')
print("USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in",country,end='.\n')
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -",0.3*moneyUSD,end='')
print("USD,",end='\n')
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",last_name)

# Program to generate a personalised spam message from Frank

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 05 March 2014

first_name = input("Enter first name:\n")

last_name = input("Enter last name:\n")

money = eval(input("Enter sum of money in USD:\n"))

country = input("Enter country name:\n")

money30 = 0.3 * money

print("\nDearest",first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk",last_name,end='')
print(", your long lost relative from Mapsfostol.")
print("My father left the sum of",money,end='')
print("USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in",country,end='')
print(".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -",money30,end='')
print("USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",last_name)


#Sample IO

#Enter first name:
#Patrick
#Enter last name:
#Star
#Enter sum of money in USD:
#1234
#Enter country name:
#South Africa

#Dearest Patrick
#It is with a heavy heart that I inform you of the death of my father,
#General Fayk Star, your long lost relative from Mapsfostol.
#My father left the sum of 1234USD for us, your distant cousins.
#Unfortunately, we cannot access the money as it is in a bank in South Africa.
#I desperately need your assistance to access this money.
#I will even pay you generously, 30% of the amount - 370.2USD,
#for your help.  Please get in touch with me at this email address asap.
#Yours sincerely
#Frank Star
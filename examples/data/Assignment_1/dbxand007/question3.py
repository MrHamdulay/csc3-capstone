# Cherise Dube
# 04 March 2014
# Program to generate a personalized spam message
first_name = input("Enter first name: \n")
last_name = input("Enter last name: \n")
money= eval(input("Enter sum of money in USD: \n"))
country = input("Enter country name: \n")
percentage = (money/100)*30

print()
print("Dearest ",first_name,"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",last_name,", your long lost relative from Mapsfostol.",sep='')
print("My father left the sum of ",money,"USD for us, your distant cousins.",sep='')
print("Unfortunately, we cannot access the money as it is in a bank in",country,end='.')
print("\nI desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",percentage,"USD,\nfor your help.  Please get in touch with me at this email address asap.",sep='')
print("Yours sincerely \nFrank",last_name) 
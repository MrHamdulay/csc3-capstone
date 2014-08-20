# Assignment 1, question 3
# Kieran Reilly, RLLKIE001
# 03/03/14
# creating a spam message

firstName = input("Enter first name: \n")
lastName = input("Enter last name: \n")
money = eval(input("Enter sum of money in USD: \n"))
country = input("Enter country name: \n")

print("");
print("Dearest "+firstName)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+lastName+", your long lost relative from Mapsfostol.")
print("My father left the sum of "+str(money)+"USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in "+country+".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - "+str(float((money*0.30)))+"USD,")   #figure how to round to 2 decimal places
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank "+lastName)




#Question 2
#Assignment1
#Sinoxolo Mpetsheni

name = input("Enter first name:\n")

surname = input("Enter last name:\n")

money = eval(input("Enter sum of money in USD:\n"))

country = input("Enter country name:\n")

percentage = (money*(30/100))

print()
print("Dearest "+name) 
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+surname+", your long lost relative from Mapsfostol.")
print("My father left the sum of ",money,"USD for us, your distant cousins.",sep="")
print("Unfortunately, we cannot access the money as it is in a bank in "+country+".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ", percentage,"USD,",sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank "+surname)
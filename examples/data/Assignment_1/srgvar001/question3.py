# program to generate to personalise spam meaasge
# SRGVAR001
# Vardhani Sarugaser
# 5/03/2014

name = input("Enter first name:\n")
last = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")


amt = (money*(30/100))

print()
print("Dearest", name)
print("It is with a heavy heart that I inform you of the death of my father,",sep="")
print("General Fayk ",last, ", your long lost relative from Mapsfostol.",sep="")
print("My father left the sum of ",money, "USD for us, your distant cousins.",sep="")
print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep="")
print("I desperately need your assistance to access this money.",sep="")
print("I will even pay you generously, 30% of the amount - ",amt,"USD,",sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank ",last,sep="")
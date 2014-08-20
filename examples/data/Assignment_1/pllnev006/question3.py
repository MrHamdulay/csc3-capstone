# Program to generate personalised spam
# Nevarr Pillay
# 25 February 2014

fname = input("Enter first name:\n")
sname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
print()


print("Dearest", fname)
print("It is with a heavy heart that I inform you of the death of my father,\n", "General Fayk ",sname, end = ", your long lost relative from Mapsfostol.\n", sep = "")
print("My father left the sum of ", money,"USD for us, your distant cousins.",sep="")
print("Unfortunately, we cannot access the money as it is in a bank in", country, end = ".\n")
print("I desperately need your assistance to access this money. \n", "I will even pay you generously, 30% of the amount - ", (money*0.3),"USD,\n", 
"for your help.  Please get in touch with me at this email address asap.\n",
"Yours sincerely\n",
"Frank ",sname, sep = "")
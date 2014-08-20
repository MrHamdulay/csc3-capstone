# Dalise Steynfaard
# STYDAL001
# Assignment 1, question 3
# 04-03-2014

f_name = input("Enter first name:\n")
l_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

print("\nDearest", f_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ", l_name, ", your long lost relative from Mapsfostol.", sep="")
print("My father left the sum of ", money, "USD ", "for us, ", "your distant cousins.", sep="")
print("Unfortunately, we cannot access the money as it is in a bank in ", country,".", sep="")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ", (money*0.3), "USD,", sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely\n", "Frank ", l_name, sep="", end="")
# Name: Hamza Ebrahim           06/03/14
# Assignment 1 CSC1015F 
# Question 3


name = input("Enter first name:\n")
surname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

print("\nDearest", name)
print("It is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk",surname, end=", "), print("your long lost relative from Mapsfostol. \nMy father left the sum of", money, end=""), print("USD for us, your distant cousins. \nUnfortunately, we cannot access the money as it is in a bank in",country, end=". "), print("\nI desperately need your assistance to access this money. \nI will even pay you generously, 30% of the amount -", (money*.3),end=""), print("USD,\nfor your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely \nFrank", surname)



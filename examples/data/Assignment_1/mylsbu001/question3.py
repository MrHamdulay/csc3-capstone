print("Enter first name:")
firstname = input()

print("Enter last name:")
lastname = input()

print("Enter sum of money in USD:")
money = eval(input())

print("Enter country name:")
country = input()

print("")
print("Dearest "+firstname)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+lastname+", your long lost relative from Mapsfostol.")
print("My father left the sum of",money,end="USD for us, your distant cousins.")
print("\nUnfortunately, we cannot access the money as it is in a bank in",country,end=".\n")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -",(money*0.3),end="USD,\n")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",lastname)

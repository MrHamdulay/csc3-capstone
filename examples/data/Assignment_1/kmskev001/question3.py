# question 3 - making a spam message
# kmskev001 kevin kumasamba
# 26/02/14

print("Enter first name: ")
name = input()
print("Enter last name: ")
surname = input()
print("Enter sum of money in USD: ")
money = eval(input())
print("Enter country name: ")
country = input()
print()

print("Dearest", name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk", surname+",", "your long lost relative from Mapsfostol.")
print("My father left the sum of ", money, "USD for us, your distant cousins.", sep=(""))
print("Unfortunately, we cannot access the money as it is in a bank in ", country, ".", sep=("")) 
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ", money*0.3,"USD", ",", sep=(""))
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", surname) 

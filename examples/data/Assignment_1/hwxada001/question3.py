#Assignment 1: Question 3:
#Author: Adam Howa
#date 06/03/2014
firstname = input("Enter first name:\n")
lastname = input("Enter last name:\n")
money = input("Enter sum of money in USD:\n")
country = input("Enter country name:\n")
money = eval(money)
tempmoney = money*0.3
print()
print("Dearest",firstname)
print("It is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk ",lastname,", your long lost relative from Mapsfostol.",sep = '')
print("My father left the sum of ",money,"USD for us, your distant cousins.",sep = '')
print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep = '')
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",tempmoney,"USD,\nfor your help.  Please get in touch with me at this email address asap.",sep = '')
print("Yours sincerely")
print("Frank",lastname)
#Author: Ross van der Heyde VHYROS001
#Date: 26 February
#Code to create a personalized spam message based on the user's inputs.

firstName = input("Enter first name:\n")
surname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
print("")

print("Dearest", firstName)
print("It is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk", surname, end="")
print(", your long lost relative from Mapsfostol.")
print("My father left the sum of ", money, "USD for us, your distant cousins.", sep ="")
print("Unfortunately, we cannot access the money as it is in a bank in ", country, ".", sep="")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ", 0.3*money, "USD,", sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely \nFrank "+ surname)
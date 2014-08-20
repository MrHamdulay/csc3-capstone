#Assignment 1, Question 3
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 27/02/2014

#Defining a function to create a spam message.

#Pre-Condition: Input first name, last name, amount of money and country.
#Post-Condition: Output the spam message.
def spamMessage():
    
    #Defining variables.
    firstName = input("Enter first name:\n")
    lastName = input("Enter last name:\n")
    amountOfMoney = eval(input("Enter sum of money in USD:\n"))
    country = input("Enter country name:\n")
    lastNameWithComma = lastName + ","
    money30 = (0.3*amountOfMoney)
    country += "."
    
    #Here several print functions are used to make it easier to read.
    print("\nDearest", firstName)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk", lastNameWithComma, "your long lost relative from Mapsfostol.")
    print("My father left the sum of ",amountOfMoney,"USD for us, your distant cousins.",sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in", country)
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ", money30, "USD,", sep="")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank", lastName)

#Generate spam message.
spamMessage()
#Johan Jansen van Vuuren
#JNSJOH014
#Assignment 1 Question 3

#Get user input
fName = input("Enter first name:\n")
lName = input("Enter last name:\n")
money = (eval(input("Enter sum of money in USD:\n")))
country = input("Enter country name:\n")

#Display output
def printOutput():
    print("\nDearest",fName)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ", lName,", your long lost relative from Mapsfostol.",sep='')
    print("My father left the sum of ",money,"USD for us, your distant cousins.",sep='')
    print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep='')
    print("I desperately need your assistance to access this money.")  
    payment = round(0.3*money,2)
    print("I will even pay you generously, 30% of the amount - ",payment,"USD,",sep='')
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",lName)
printOutput()
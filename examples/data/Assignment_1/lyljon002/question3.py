# Question 3, Assignment 1
# Jonathan Leyland, LYLJON002  
# 1 March 2014


Name = input("Enter first name:\n")
Surname = input("Enter last name:\n")
Money = eval(input("Enter sum of money in USD:\n"))
Country = input("Enter country name:\n")

print("\nDearest",Name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ",Surname,", your long lost relative from Mapsfostol.",sep='')
print("My father left the sum of ",Money,"USD for us, your distant cousins.",sep='')
print("Unfortunately, we cannot access the money as it is in a bank in",Country,end='.')
print("\nI desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",(Money*0.3),"USD,",sep='')
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",Surname)
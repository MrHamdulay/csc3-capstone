#Assignment 1
# Question 3

fn = input("Enter first name:\n")

ln = input("Enter last name:\n")

usd = eval(input("Enter sum of money in USD:\n"))

count = input("Enter country name:\n")

x = (usd* 30/100)
#print(x)
# incorrect spacing at variable positions
print("\nDearest", fn)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ",ln,", your long lost relative from Mapsfostol.",sep='')
print("My father left the sum of ",usd,"USD for us, your distant cousins.", sep ='')
print("Unfortunately, we cannot access the money as it is in a bank in ",count,".", sep ='')
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",x,"USD,", sep ='')
print("for your help.  Please get in touch with me at this email address asap.\nYours sincerely")
print("Frank",ln)



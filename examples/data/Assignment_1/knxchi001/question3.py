# Practical Assignment 1
# Question 3

print("Enter first name:", end="\n")
first_name = input()
print("Enter last name:", end="\n")
last_name = input()
print("Enter sum of money in USD:",end="\n")
money= eval(input())
print("Enter country name:",end="\n")
country= input()
money30= 0.3*money
print()
print("Dearest",first_name)
print("It is with a heavy heart that I inform you of the death of my father,") 
print("General Fayk ",last_name,", your long lost relative from Mapsfostol.",sep="")
print("My father left the sum of ",money,"USD for us, your distant cousins.",sep="")
print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep="")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",money30,"USD,",sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",last_name)



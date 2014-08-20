#spam email

first_name=input("Enter first name:\n")
last_name=input("Enter last name:\n")
money=eval(input("Enter sum of money in USD:\n"))
money30= 0.3*money
country=input("Enter country name:\n")
# \n in this line causes two new lines
print("\n" "Dearest" , first_name) # \n in front of a print function will put it in a new line
print("It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk" , last_name, end="," " your long lost relative from Mapsfostol." "\n") 
print("My father left the sum of" , money, end="USD" " for us, your distant cousins." "\n")
print("Unfortunately, we cannot access the money as it is in a bank in" , country, end="." "\n")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -" , money30, end="USD," "\n")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank" , last_name)

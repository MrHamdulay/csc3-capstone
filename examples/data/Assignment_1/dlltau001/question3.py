#Question 3 - Assignment 1
#Author : Tauriq Dolley

firstname = input("Enter first name: \n")
secondname = input("Enter last name: \n")
amount = input("Enter sum of money in USD: \n")
country = input("Enter country name: \n")

money = eval(amount)
percentage = (money/100)*30

print()

print("Dearest "+firstname+
"\nIt is with a heavy heart that I inform you of the death of my father,",
"General Fayk "+secondname+", your long lost relative from Mapsfostol.",
"My father left the sum of "+amount+"USD for us, your distant cousins.",
"Unfortunately, we cannot access the money as it is in a bank in "+country+".",
"I desperately need your assistance to access this money.",
"I will even pay you generously, 30% of the amount - "+str(percentage)+"USD,",
"for your help.  Please get in touch with me at this email address asap.",
"Yours sincerely",
"Frank "+secondname,sep="\n")



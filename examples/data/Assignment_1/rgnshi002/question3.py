# Program to create a spam message based on details of user
# Shivam Ragoonaden
# 28 February 2014

Name = input("Enter first name:\n")
Last_Name = input("Enter last name:\n")
Money = eval(input("Enter sum of money in USD:\n"))
Country = input("Enter country name:\n")

print("")
MoneyPer = Money*0.3

Money = str(Money)
MoneyPer = str(MoneyPer)

print("Dearest "+ Name+"\n"
"It is with a heavy heart that I inform you of the death of my father,\n"
"General Fayk "+Last_Name +", your long lost relative from Mapsfostol.\n"
"My father left the sum of "+Money+"USD for us, your distant cousins.\n"
"Unfortunately, we cannot access the money as it is in a bank in "+Country+".\n"
"I desperately need your assistance to access this money.\n"
"I will even pay you generously, 30% of the amount - " +MoneyPer+"USD,\n"
"for your help.  Please get in touch with me at this email address asap.\n"
"Yours sincerely\n"
"Frank",Last_Name)
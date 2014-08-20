#MSG_GEN
#Grant Meeser MSRGRA002
#26/02/2014

#get user data
firstName = input("Enter first name:\n")
lastName = input("Enter last name:\n")
money = input("Enter sum of money in USD:\n")
country = input("Enter country name:\n")

#calculate 30% of money
money30 = str(eval(money)*0.3)

#print message
print("\nDearest "+firstName,"It is with a heavy heart that I inform you of the death of my father,","General Fayk "+lastName+", your long lost relative from Mapsfostol.","My father left the sum of "+money+"USD for us, your distant cousins.","Unfortunately, we cannot access the money as it is in a bank in "+country+".","I desperately need your assistance to access this money.","I will even pay you generously, 30% of the amount - "+money30+"USD,","for your help.  Please get in touch with me at this email address asap.","Yours sincerely","Frank "+lastName,sep="\n")

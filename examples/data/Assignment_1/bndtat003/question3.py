# Program to check the validity of the time entered

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 04-02-2014


name1 = input('Enter first name:\n')

name2 = input('Enter last name:\n')

money = input('Enter sum of money in USD:\n')

country = input('Enter country name:\n')

money2 = eval(money)

amount = money2*(30/100)

print('')

print("Dearest ",name1,'\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ',name2,', your long lost relative from Mapsfostol.\nMy father left the sum of ',money,'USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ',country,'.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ',amount,'USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ',name2,sep='')

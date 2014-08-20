#Teko Ntimane
#Question 3

FName = input("Enter first name:\n")
LName = input("Enter last name:\n")
Money = eval(input("Enter sum of money in USD:\n"))
Country = input("Enter country name:\n")

NewMoney = Money * 30 / 100
    
print("")
print("Dearest", FName)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk ', LName, ', your long lost relative from Mapsfostol.', sep='')
print('My father left the sum of ', Money, 'USD for us, your distant cousins.', sep='')
print('Unfortunately, we cannot access the money as it is in a bank in ', Country, '.', sep='')
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount - ', NewMoney, 'USD,',sep="")
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely')
print('Frank', LName)
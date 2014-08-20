#Spam Generator
#Tashiv Sewpersad
#25-02-2014

sFirstName = input("Enter first name:"+"\n")
sLastName = input("Enter last name:"+"\n")
iMoney = eval(input("Enter sum of money in USD:"+"\n"))
sCountry = input("Enter country name:"+"\n")

iMoneyAward = (iMoney/100)*30

sMessage = "Dearest " + sFirstName + "\n"
sMessage = sMessage + "It is with a heavy heart that I inform you of the death of my father," + "\n" + "General Fayk " + sLastName + ", your long lost relative from Mapsfostol." + "\n" + "My father left the sum of " + str(iMoney) + "USD for us, your distant cousins." + "\n" + "Unfortunately, we cannot access the money as it is in a bank in " + sCountry + "." + "\n" + "I desperately need your assistance to access this money." + "\n" + "I will even pay you generously, 30% of the amount - " + str(iMoneyAward) + "USD," + "\n" + "for your help. " + " Please get in touch with me at this email address asap."
sMessage = sMessage + "\n" + "Yours sincerely" + "\n" + "Frank " + sLastName

print("\n",sMessage, sep="")
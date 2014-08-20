#Sphiwe Muthembi
#Student number : MTHSPH007
#Date : 25/02/2014
#A program to send a person a personalised spam message

Name= input("Enter first name:\n")
Surname= input("Enter last name:\n")
Money= eval(input("Enter sum of money in USD:\n"))
Country= input("Enter country name:\n")
Money2 = Money*30/100


    
#print("\n")
print("Dearest",Name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk",Surname+", your long lost relative from Mapsfostol.")
print("My father left the sum of",str(Money)+"USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in",Country,end=".\n")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -",str(Money2)+"USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",Surname)

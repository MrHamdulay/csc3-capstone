#Question 3
#Spam Message
#Tase Ngambi
#NGMTAS001
#25/02/2014


def SpamMess():
    firstName = input("Enter first name:\n")
    lastName = input("Enter last name:\n")
    sumMoney = eval(input("Enter sum of money in USD:\n" ))
    country = input("Enter country name:\n")
    
    print("\nDearest",firstName)
    print("It is with a heavy heart that I inform you of the death of my father,")      
    print("General Fayk ", lastName ,', your long lost relative from Mapsfostol.', sep ="")
    print("My father left the sum of ", sumMoney,'USD for us, your distant cousins.', sep ="")
    print("Unfortunately, we cannot access the money as it is in a bank in ", country,".", sep ="")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ", str((0.3*sumMoney)),'',"USD,", sep ="") #convert number to string
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank", lastName)
    
    
SpamMess()    
   





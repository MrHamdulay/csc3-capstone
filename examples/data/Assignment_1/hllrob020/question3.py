#Personal Spam programme
#Robin Hall
#25/02/2014

def personalspam():
    name=input("Enter first name:\n")
    last_name=input("Enter last name:\n")
    money=eval(input("Enter sum of money in USD:\n"))
    money_percent=0.3*money
    country=input("Enter country name:\n")
    
    print("\nDearest ",name,"\n","It is with a heavy heart that I inform you of the death of my father,\n","General Fayk ",last_name,", your long lost relative from Mapsfostol.\n","My father left the sum of ",money,"USD for us, your distant cousins.\n","Unfortunately, we cannot access the money as it is in a bank in ",country,".\n","I desperately need your assistance to access this money.\n","I will even pay you generously, 30% of the amount - ",money_percent,"USD,\n","for your help.  Please get in touch with me at this email address asap.\n","Yours sincerely\n","Frank ",last_name,sep="")

personalspam()
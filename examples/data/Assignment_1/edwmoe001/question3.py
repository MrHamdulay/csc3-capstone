def main():
    FN=input("Enter first name: \n")
    LN=input("Enter last name: \n")
    money=eval(input("Enter sum of money in USD: \n"))
    money30=str(money*0.3)
    country=input("Enter country name: \n")
    print()
    print("Dearest",FN)
    print("It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",LN,", your long lost relative from Mapsfostol.\nMy father left the sum of ",money,"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ",country,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",money30,'USD,',sep="")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely\n","Frank ", LN, sep="")
    
main()

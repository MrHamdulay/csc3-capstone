def intake():
    first_name=input('Enter first name: \n')
    last_name=input('Enter last name: \n')
    money=eval(input('Enter sum of money in USD: \n'))
    country=input('Enter country name: \n')
    k=0.3*money
    def output():
        print("\nDearest {0}\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk {1}, your long lost relative from Mapsfostol.\nMy father left the sum of {2}USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in {3}.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - {4}USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank {1}".format(first_name,last_name,money,country,k)) 
        
    output()    
intake()

    


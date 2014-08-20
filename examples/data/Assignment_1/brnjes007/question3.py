def spam():    
    x=(input("Enter first name:"))
    y=(input("Enter last name:"))
    z=(input("Enter sum of money in USD:"))
    w=(input("Enter country name:"))
    
    line1=("\n Dearest {0}\n It is with a heavy heart that I inform you of the death of my father,\n General Fayk {1}, your long lost relative from Mapsfostol.\n My father left the sum of {2}USD for us, your distant cousins.\n Unfortunately, we cannot access the money as it is in a bank in {3}.\n I desperately need your assistance to access this money.\n I will even pay you generously, 30% of the amount - {2}USD,\n for your help.  Please get in touch with me at this email address asap.\n Yours sincerely\n Frank {1}")

    print(line1.format(x,y,z,w))
   
    
if __name__=='__main__':
        spam()
    
    
#Dumisani Nyathi
#program with a letter
#assignment1

def money():
    nme=input("Enter first name:"'\n')
    srnme=input("Enter last name:"'\n')
    csh=eval(input("Enter sum of money in USD:"'\n'))
    cntry=input("Enter country name:"'\n')
    cut=(30*csh)/100
    print("\nDearest ",nme,'\n'"It is with a heavy heart that I inform you of the death of my father,",'\n'"General Fayk ",srnme,", your long lost relative from Mapsfostol.",'\n'"My father left the sum of ",csh,"USD for us, your distant cousins.",'\n'"Unfortunately, we cannot access the money as it is in a bank in ",cntry,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",cut,"USD,",'\n'"for your help.  Please get in touch with me at this email address asap.",'\n'"Yours sincerely",'\n'"Frank ",srnme,sep="")

money()
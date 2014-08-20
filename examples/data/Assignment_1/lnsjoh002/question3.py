#program to create a spam message
#JP Lanser
#25 feb 2014


def main():
    name=input("Enter first name:\n")
    surname=input("Enter last name:\n")
    money=eval(input("Enter sum of money in USD:\n"))
    country=input("Enter country name:\n")
    
    print()
    print("Dearest",name,)    
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk",surname, end="" ", your long lost relative from Mapsfostol.\n")
    print("My father left the sum of",money, end="" "USD for us, your distant cousins.\n")
    print("Unfortunately, we cannot access the money as it is in a bank in", country, end="." "\n")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount -",0.3*money, end="" "USD, \n")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank", surname)
        
          
          
main()

  

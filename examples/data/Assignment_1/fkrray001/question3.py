# Author : Rayaan Fakier FKRRAY001
# Date : 28 - 02 - 2014

# Define main function
def main(): 
    # Take inputs for the mark's details
    get_Name = input("Enter first name:\n")
    get_LastName = input("Enter last name: \n")
    get_Money = input("Enter sum of money in USD:\n")
    get_Nationality = input("Enter country name:\n")

    # Create money30 as a function of get_Money
    money30 = int(get_Money) * 0.3
    
    # output message of spam
    print (" \nDearest", get_Name)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk", get_LastName + ",", "your long lost relative from Mapsfostol.")
    print("My father left the sum of", get_Money + "USD" , "for us, your distant cousins.")
    print("Unfortunately, we cannot access the money as it is in a bank in",  get_Nationality + ".")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount -", str(money30) + "USD,")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank" , get_LastName)
# call main function
main()
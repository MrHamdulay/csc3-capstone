#A program to generate a personalised spam message
#by Mulaudzi Khumbelo Lucius
#MLDLUC002

def main():
    
    first_name=input("Enter first name:")
    last_name=input("Enter last name:")
    money=input("Enter sum of money in USD:")
    country=input("Enter country name:")
    money30=money*(30/100)
 

    print("It is with a heavy heart that I inform you of the death of my father sep=","General Fays",last_name,"your long lost relative from Mapsfostol.\n")
    print("My father left the sum of",money,"USD for us,your distant cousin.\n")
    print("Unfortunately,we cannot access the money as it it in a bank in",country,".\n")
    print("I desperately need your assistance to access this money.\n")
    print("I will even pay you generously, 30% of the amount" - money30,"USD,for you help.\n")
    print("Please get in touch with me at this email address asap.\n")
    print("Yours sincerely\n")
    print("Frank",last_name)

    print()
    
main()
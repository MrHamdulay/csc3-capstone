#Phumelele Ndimande
#Question 3

def main():
    
    first_name = input("Enter the first name:\n")
    last_name = input("Enter the last name:\n")
    Money = eval(input("Enter sum of money in USD:\n"))
    country = input("Enter the country name:\n")
    Money30 = Money * 30/100
    
    if Money > 0: 
        
        print("\nDearest", first_name, "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk", last_name, ", your long lost relative from Mapsfostol.")
        print("My father left the sum of money", Money,"USD for us, your distant cousins.")
        print("Unfortunately, we cannot access the money as it is in a bank in", country) 
        print("I desperately need your assistance to access this money.")
        print("I will even pay you generously, 30% of the amount -", Money30,"USD,\nfor your help. Please get in touch with me at this email address asap.\nYours sincerely\nFrank", last_name)
    else:
            print("")

main()
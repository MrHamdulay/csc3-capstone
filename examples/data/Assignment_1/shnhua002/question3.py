#Spam generator
#Assignment 1, Question 3
#Charlie Shang  SHNHUA002

Name = input("Enter first name:\n")
Surname = input("Enter last name:\n")
Amount = eval(input("Enter sum of money in USD:\n"))
Country = input("Enter country name:\n")

def mail(name,surname,amount,country):
    print("\nDearest ", name, "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ", surname , ", your long lost relative from Mapsfostol.\n" "My father left the sum of ", amount, "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ", country, ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ", (0.3*amount), "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ", surname, sep=(""))

mail(Name,Surname,Amount,Country)    
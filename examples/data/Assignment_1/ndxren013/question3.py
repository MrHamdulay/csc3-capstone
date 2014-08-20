import math

def main ():
    
    first_name = input("Enter first name:\n")
    last_name = input("Enter last name:\n")
    money = input("Enter sum of money in USD:\n")
    country = input("Enter country name:\n")
    last_name = last_name+","
    value = eval(money)
    value = value*3/10
    value = str(value)
    value = value+"USD,"
    money = money+"USD"
    country = country+"."
    
    
    print()
    
    print("Dearest",first_name,"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk", last_name, "your long lost relative from Mapsfostol.\nMy father left the sum of", money, "for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in", country, "\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount -", value, "\nfor your help.", end = "")
    length = len(last_name)
    last_name = last_name[0:length-1]
    print("  Please get in touch with me at this email address asap.\nYours sincerely\nFrank", last_name)
    
main()
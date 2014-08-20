# Question 3
# Name: Khanyisile Morudu
# Student Number: mrdkha001
# Date: 05/03/2014

def spam(a,b,c,d,e):
    message = "\nDearest " + first_name + " \nIt is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk " + last_name+ ", your long lost relative from Mapsfostol.\nMy father left the sum of " + moneyUSD1 + " for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in "+ country + ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - " + moneyUSD2 + ",\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely \nFrank "  + last_name
    print(message)
    
first_name = input("Enter first name: \n")
last_name =  input("Enter last name: \n")
money = eval(input("Enter sum of money in USD: \n"))
country = input("Enter country name: \n")
moneyUSD1 = str(money) + "USD"
money30 = money * (30/100)
moneyUSD2 = str(money30) + "USD"
spam(first_name,last_name, moneyUSD1, country, moneyUSD2)
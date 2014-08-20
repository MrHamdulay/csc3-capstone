# kemeshan naicker 
# 3 march 2014
# program to generate a personalised spam message

a = input("Enter first name: \n")
b = input("Enter last name: \n")
c = eval(input("Enter sum of money in USD: \n"))
d = input("Enter country name: \n")
e = 0.3*c

print("\nDearest ", a, "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ", b,", your long lost relative from Mapsfostol.\nMy father left the sum of ", c,"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ", d,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ", round(e, 2), "USD, \nfor your help.  Please get in touch with me at this email address asap. \nYours sincerely \nFrank ", b, sep=(""))
      
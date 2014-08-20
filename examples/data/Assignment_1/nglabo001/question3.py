"""fn is first name
ln is last name
total_amount is sum of money
cn is country name
tp is thirty percent of the money
"""
fn = input('Enter first name:\n')
ln = input('Enter last name:\n')
total_amount = eval(input("Enter sum of money in USD:\n"))
cn = input("Enter country name:\n")

tp = total_amount*0.3



print("\nDearest ",fn,"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",ln,", your long lost relative from Mapsfostol.\nMy father left the sum of ",total_amount,"USD"," for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ",cn,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",tp,"USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ",ln,sep='')


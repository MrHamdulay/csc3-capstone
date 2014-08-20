#program to generate personalised spam message
#4 march 2014
#vuyolwethu nkosi

w=input("Enter first name:\n")
x=input("Enter last name:\n")
y=eval(input("Enter sum of money in USD:\n"))
z=input("Enter country name:\n")

print("\nDearest ",w,"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",x,", your long lost relative from Mapsfostol.\nMy father left the sum of ",y, "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ",z,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",y*30/100,"USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely \nFrank ",x,sep="")
#generate spam message
#Micaela Menegaldo

fname=input("Enter first name:" "\n")

lname=input("Enter last name:" "\n")

money=input("Enter sum of money in USD:" "\n")
money=eval(money)
percentage=money/100*30
round(percentage)

country=input("Enter country name:" "\n")



print("\n" "Dearest", fname)
print("It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",lname, ", your long lost relative from Mapsfostol.\nMy father left the sum of ", money,"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ", country,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",percentage,"USD,\nfor your help.  Please get in touch with me at this email address asap.",sep="")
print("Yours sincerely")
print("Frank", lname)
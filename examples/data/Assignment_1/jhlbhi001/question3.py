#question_3.py
#spam letter
#by Bhishum Jahaly
first_name=input("Enter first name:\n")
last_name=input("Enter last name:\n")
sum_of_money=int(input("Enter sum of money in USD:\n"))
country=input("Enter country name:\n")
p=(0.3*sum_of_money)
print("")
print("Dearest",first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ", last_name,", your long lost relative from Mapsfostol.",sep="")
print("My father left the sum of ", sum_of_money,"USD for us, your distant cousins.",sep="")
print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep="")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - " ,p,"USD,",sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",last_name)
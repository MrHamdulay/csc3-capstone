#Question 3: Assignment 1
#Tashfia Amin
#AMNTAS003

def spam():
    a=input("Enter first name: \n")
    b=input("Enter last name: \n")
    c=input("Enter sum of money in USD: \n")
    d=input("Enter country name: \n")
    e=str(float(c)*0.3)
    print(" ")
    
    print("Dearest", a)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk", b+",", "your long lost relative from Mapsfostol.")
    print("My father left the sum of", c+"USD for us, your distant cousins.")
    print("Unfortunately, we cannot access the money as it is in a bank in", d+".")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount -", e+"USD,")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank", b)
    
spam()

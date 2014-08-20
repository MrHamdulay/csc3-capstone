# question3.py
# A program to generate a personalised spam message based on the user's full name, country and a sum of money
# Created by : Sibabalwe Qamata
#Date : 05 March 2014

def main():
 FirstName=input("Enter first name:")
 LastName=input("Enter last name:")
 Money=eval(input("Enter sum of money in USD:"))
 Country=input("Enter Country name:")
 Percentage=Money*(30//100)

 print("Dearest",FirstName)
 print("It is with a heavy heart that I inform you of the death of my father,General",LastName," your long lost relative from Mapsfostol.")
 print("My father left the sum of ",Money,"USD for us, your distant cousins.")
 print("Unfortunately, we cannot access the money as it is in a bank in Springfiels. ")
 print("I desperately need your assistance to access this money.")
 print("I will even pay you generously, 30% of the amount -",Percentage," USD for your help.")  
 print("Please get in touch with me at this email address asap.")
 print("Yours sincerely.")
 print("Frank", LastName)
main()

 # a program to generate a personalised spam message based on the user's full name, country and a sum of money.
 # by Fadzai Mupfunya
 # 26 February 2014
 
def main():
  first_name = input("Enter first name: "'\n')
  last_name = input("Enter last name: "'\n')
  money = input("Enter sum of money in USD: "'\n')
  money=eval(money)
  percentage=float((money*0.3))
  country = input("Enter country name: " '\n') 
  print()
  print("Dearest", first_name,)
  print("It is with a heavy heart that I inform you of the death of my father,")
  print("General Fayk ",last_name,", your long lost relative from Mapsfostol.",sep="")
  print("My father left the sum of ",money,"USD for us, your distant cousins.",sep="")
  print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep="")
  print("I desperately need your assistance to access this money.")
  print("I will even pay you generously, 30% of the amount - ",percentage,"USD,",sep="")
  print("for your help.  Please get in touch with me at this email address asap.")
  print("Yours sincerely")
  print("Frank",last_name)


main()
 
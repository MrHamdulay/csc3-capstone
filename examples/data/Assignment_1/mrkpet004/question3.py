# program to check the validity of a time
# Peter Muriuki
# 25 february 2014

first_name = 0    # variable to store user's input for first name
last_name = 0     # variable to store user's input for last name
money = 0         # variable to store user's input for amount of money in USD
country = 0       # variable to store user's input for name of country

first_name =input("Enter first name:\n")
last_name =input("Enter last name:\n")
money =eval(input("Enter sum of money in USD:\n"))
country =input("Enter country name:\n")
money30 = (money*3/10)

print ("\nDearest",first_name,)
print ("It is with a heavy heart that I inform you of the death of my father,")
print ("General Fayk ",last_name, ", your long lost relative from Mapsfostol.",sep="")
print ("My father left the sum of " ,money,"USD for us, your distant cousins.",sep="")
print ("Unfortunately, we cannot access the money as it is in a bank in",country+".")
print ("I desperately need your assistance to access this money.")
print ("I will even pay you generously,"" 30%"," of the amount"," - ",money30,"USD,",sep="")
print ("for your help.","","Please get in touch with me at this email address asap.")
print ("Yours sincerely")
print ("Frank",last_name)
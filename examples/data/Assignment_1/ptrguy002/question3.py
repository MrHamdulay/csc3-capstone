fname = input("Enter first name:\n")
lname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
money30 = 0.3*money

print("""\nDearest %s
It is with a heavy heart that I inform you of the death of my father,
General Fayk %s, your long lost relative from Mapsfostol.
My father left the sum of %dUSD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in %s.
I desperately need your assistance to access this money.
I will even pay you generously, 30%% of the amount - %.1fUSD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank %s""" % (
        fname,
        lname,
        money,
        country,
        money30,
        lname
))

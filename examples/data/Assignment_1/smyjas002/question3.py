nameFirst = input('Enter first name:\n')
nameLast = input('Enter last name:\n')
money = input('Enter sum of money in USD:\n')
subMoney = str(eval(money) * 0.3)
country = input('Enter country name:\n')

stringSpam = "\nDearest " + nameFirst + "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk " + nameLast + ", your long lost relative from Mapsfostol.\nMy father left the sum of " + money + "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in " + country + ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - " + subMoney + "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank " + nameLast

print(stringSpam)
"""
Dearest <first_name>
It is with a heavy heart that I inform you of the death of my father,
General Fayk <last_name>, your long lost relative from Mapsfostol.
My father left the sum of <money>USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in <country>.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - <money30>USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank <last_name>

Sample IO

Enter first name:
Patrick
Enter last name:
Star
Enter sum of money in USD:
1234
Enter country name:
South Africa

Dearest Patrick
It is with a heavy heart that I inform you of the death of my father,
General Fayk Star, your long lost relative from Mapsfostol.
My father left the sum of 1234USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in South Africa.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - 370.2USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank Star
"""

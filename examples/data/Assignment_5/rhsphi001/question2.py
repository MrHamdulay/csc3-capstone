'''  a program to simulate a vending machine and calculate change based on the amount paid
     Phillip Ruhesi
     16 April 2014'''
cost=eval(input('Enter the cost (in cents):\n')) #prompts users to enter cost
amount=0
while amount<cost:
    money=eval(input('Deposit a coin or note (in cents):\n')) #checks wether the amount of money is enough to cover the cost
    amount=amount+money
if amount!=cost:
    print('Your change is:')
change=amount-cost
dollar=change//100                    # Calculates the change in denominations: 1c, 5c, 10c, 25c, $1
Twentyfivecents=(change%100)//25
Tencents=((change%100)%25)//10
Fivecents=(((change%100)%25)%10)//5
Onecent=((((change%100)%25)%10)%5)
if dollar>0: 
    print(dollar,'x $1')
if Twentyfivecents>0:
    print(Twentyfivecents,'x 25c')
if Tencents>0:
    print(Tencents,'x 10c')           # prints the amount in a specific format
if Fivecents>0:
    print(Fivecents,'x 5c')
if Onecent>0:
    print(Onecent,'x 1c')
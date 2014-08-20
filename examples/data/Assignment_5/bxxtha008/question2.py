""" program to simulate vending machine & calculate change based on amount paid by customer
Thabiso Beau
15 April 2014"""

x=eval(input('Enter the cost (in cents): \n'))
y=0
while x>y:
    z=eval(input('Deposit a coin or note (in cents): \n'))
    y += z
a=y-x

if a!=0:
    print('Your change is:')
        #testing chsnge for $1 denominations
    if a//100>0:
        dollar = (a//100)
        print(dollar, "x $1")
        #continuing the statement with the variable and finding the remainder in order to test for 25c denominations
        a = a-(dollar*100)
    #testing change for 25c statements
    if a//25>0:
        quarter = (a//25)
        print(quarter, "x 25c")
        #continuing statement with variable and finding remainder in order to test for 10c denominations
        a= a -(quarter*25)
    #testing change for 10c statements
    if a//10>0:
        ten_cent = (a//10)
        print(ten_cent, "x 10c")
        #continuing statement with variable and finding remainder in order to test for 5c denominations
        a= a - (ten_cent*10)
        #testing change for 5c statements
    if a//5:
        five_cent = (a//5)
        print(five_cent, "x 5c")
        #continuing statement with variable and finding remainder in order to test for 1c denominations
        a = a-(five_cent*5)
    #testing change for 1c statements
    if 0<a<5:
        print(a, "x 1c")
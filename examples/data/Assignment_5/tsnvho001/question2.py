#Program to Simulate a vending machine, taking user input and returning remainder
#Tsanwani Vhonani
#15 April 2014

def change():
    cost=eval(input("Enter the cost (in cents):\n"))
    deposit=0
    while deposit<cost:
        deposit+=eval(input("Deposit a coin or note (in cents):\n"))
    if deposit>cost:
        change=deposit-cost
        if change!=0:
            print("Your change is:")
        dollars=change//100
        if dollars!=0:
            print(dollars,'x $1')
        cents=(change-dollars*100)//25
        if cents!=0:
            print(cents,'x 25c')
        ten_cents=(change-dollars*100-cents*25)//10
        if ten_cents!=0:
            print(ten_cents,'x 10c')
        five_cents =(change-dollars*100-cents*25-ten_cents*10)//5
        if five_cents!=0:
            print(five_cents,'x 5c')
        one_cents=(change-dollars*100-cents*25-ten_cents*10-five_cents*5)//1
        if one_cents!=0:
            print(one_cents,'x 1c')
            
change()


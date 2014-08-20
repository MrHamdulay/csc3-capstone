x=eval(input("Enter the cost (in cents):\n"))

payment=0

while payment<x:
    y=eval(input("Deposit a coin or note (in cents): \n"))
    payment+=y
    
change=payment-x
if change!=0:
    print("Your change is:")
       
one_dollar=change//100
twenty_five=(change%100)//25
ten=((change%100)%25)//10
five=(((change%100)%25)%10)//5
one=((((change%100)%25)%10)%5)//1


if one_dollar>0:
        print(one_dollar,"x $1")
if twenty_five>0:
        print(twenty_five,"x 25c")
if ten>0:
        print(ten,"x 10c")
if five>0:
        print(five,"x 5c")
if one>0:
        print(one,"x 1c")
        
""" my own vending machine
roger cox
16/04/2014"""

cost=eval(input("Enter the cost (in cents):\n"))
paid=0
#always enter the cost
while cost>paid:

    paid+=eval(input("Deposit a coin or note (in cents):\n"))
    #the while loop runs until cost<paid 
if (cost!=paid):
    print("Your change is:")
#only if there is change    
change= paid-cost

dollar=change//100

if(dollar>=1):
    print(dollar,"x $1")
    # how many dollars change
    
rem_1=change%100
quater_cent=rem_1//25

if(quater_cent>=1):
    print(quater_cent,"x 25c")
    # how many 25c change
    
rem_2=rem_1%25
c_10=rem_2//10
if(c_10>=1):
    print(c_10,"x 10c")
    #how many 10c change
    
rem_3=rem_2%10
c_5=rem_3//5
if(c_5>=1):
    print(c_5,"x 5c")
    #how many 5c change
    
if((rem_3%5)>=1):
    print (rem_3,"x 1c")
    # how many 1c change

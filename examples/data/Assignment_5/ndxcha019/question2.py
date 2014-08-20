'''Luke Naude
program to calculate change
13 April'''

#get input
cost=eval(input('Enter the cost (in cents):\n'))
payment=0 #payment to begin with

#user continues to input money till enough
while payment<cost: 
    payment_entered=eval(input('Deposit a coin or note (in cents):\n'))
    payment+=payment_entered

#finding extra 
change=payment-cost

#convert change to coin values
dollar_change=change//100
rem_1=change%100
fifty_c_change=rem_1//50
rem_2=rem_1%50
twentyfive_c_change=rem_2//25
rem_3=rem_2%25
ten_c_change=rem_3//10
rem_4=rem_3%10
five_c_change=rem_4//5
rem_5=rem_4%5
one_c_change=rem_5//1


#tell user the change
if change != 0:
    
    print('Your change is:')
    if dollar_change!=0:
        print(dollar_change,' x $1',sep='')
    if fifty_c_change!=0:
        print(fifty_c_change,' x 50c',sep='')
    if twentyfive_c_change !=0:
        print(twentyfive_c_change,' x 25c',sep='')
    if ten_c_change!=0:
        print(ten_c_change,' x 10c',sep='')
    if five_c_change!=0:
        print(five_c_change,' x 5c',sep='')
    if one_c_change!=0:
        print(one_c_change,' x 1c',sep='')



    

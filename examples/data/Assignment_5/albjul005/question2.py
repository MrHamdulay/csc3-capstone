""" Vending Machine Program
Julian Albert
ALBJUL005
15-04-2014"""

#Defining the change values
def coins(cents):
    cents25 = cents//25
    cents=cents%25

    cents10 = cents//10
    cents=cents%10
    
    cents5 = cents//5
    cents=cents%5    

    cents1 = cents//1
    cents=cents%1
    #sets an output function
    output=''
    if cents25>0: output+='\n'+str(cents25)+' x 25c'
    if cents10>0: output+='\n'+str(cents10)+' x 10c'
    if cents5>0: output+='\n'+str(cents5)+' x 5c'
    if cents1>0: output+='\n'+str(cents1)+' x 1c'
    
    return output
#users input  

cost = eval(input('Enter the cost (in cents): ''\n'))
if cost != 0:
    deposit = eval(input('Deposit a coin or note (in cents): ''\n'))
    while deposit < cost:
        deposit += eval(input('Deposit a coin or note (in cents): ''\n'))
    if deposit > cost: #accounts for deposit being correct first time
        remainder = deposit - cost
        if remainder//100>0:
            dollar = ('\n'+str(remainder//100)+' x $1')
        else:
            dollar=''
        print('Your change is: ',dollar,coins(remainder%100), sep='')
    
elif cost ==0:
    print('')    
#loop continues until correct deposit is reached



        
        
       

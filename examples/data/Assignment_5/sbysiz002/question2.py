cost = eval(input('Enter the cost (in cents):\n'))
paid=0
while cost > paid :
    paid+=eval(input('Deposit a coin or note (in cents):\n'))
Change= paid - cost 
Change1=(Change//100)
rem0=(Change%100)
Change2=(rem0//25)
rem1=(rem0%25)
Change3=(rem1//10)
rem2=(rem1%10)
Change4=(rem2//5)
rem3=(rem2%5)
Change5=(rem3//1)
if Change != 0:
    print('Your change is:')   
if Change1 != 0 :
    print(Change1,'x $1')
if Change2 != 0:    
    print(Change2,'x 25c')
if Change3 != 0:    
    print(Change3,'x 10c')
if Change4 != 0:    
    print(Change4,'x 5c')
if Change5 != 0: 
    print(Change5,'x 1c')
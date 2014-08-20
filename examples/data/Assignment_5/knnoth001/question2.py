'''Programs that gives changes in $1, 25c, 10c, 5c and 1c 
 Name: Othniel KONAN
 Student number: KNNOTH001
 Date: 2014/04/12'''

#definition of variable
cost = eval(input('Enter the cost (in cents):\n'))
total_deposit = 0

#ask the user to put more money until it is enough to covert the cost
while total_deposit < cost:
    deposit = eval(input('Deposit a coin or note (in cents):\n'))
    total_deposit += deposit

change = total_deposit - cost
if change!= 0:
    print('Your change is:')

#the following 'if' condition works excatly the same way
 
if change >= 100:           #check if the change can be given using $1
    dollar = change // 100  #make 'dollar' the number of dollar that can be given
    change = change % 100   #make 'change' the change after the previous operation
    print(dollar,'x','$1')  #print the number of dollar that can be given
if change >= 25:
    c_25 = change // 25
    change = change % 25 
    print(c_25,'x','25c')
if change >= 10:
    c_10 = change // 10
    change = change % 10 
    print(c_10,'x','10c')
if change >= 25:
    c_5 = change // 5
    change = change % 5 
    print(c_5,'x','5c')
elif change > 1:            #this instruction is executed if and only if 0<change<5 so...
    print(change,'x','1c')

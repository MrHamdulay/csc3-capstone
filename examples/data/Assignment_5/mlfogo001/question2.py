cost = eval(input('Enter the cost (in cents):'))
dep=0


while cost>dep:
    print()
    dep+= eval(input('Deposit a coin or note (in cents):'))
    
    
    

change= dep - cost
dol = change//100
quar = (change%100)//25
ten = ((change%100)%25)//10
fiv = (((change%100)%25)%10)//5
one = (((change%100)%25)%10)%5

if cost==0:
    print("")
if cost==dep:
    print("")
else:    
    print('\nYour change is:')
if dol>0:
    print(dol,'x $1')
    
if quar>0:
    print(quar,'x 25c')

if ten>0:
    print(ten,'x 10c')
    
if fiv>0:
    print(fiv,'x 5c')

if one>0:
    print(one,'x 1c')
              
              
          
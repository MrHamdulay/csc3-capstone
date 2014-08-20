cost = eval (input("Enter the cost (in cents):\n"))

deposit = 0

while deposit < cost: 
    insert = eval(input("Deposit a coin or note (in cents): \n"))
    deposit= deposit + insert
    
change = deposit - cost
if change != 0:
    print('Your change is: ')
    dollars = change//100
    change = change - (dollars*100)
    if dollars != 0:
        print(dollars, 'x $1')
    quarter = change// 25
    change = change -(quarter*25)
    if quarter != 0:
        print(quarter, "x 25c")
    tenc = change//10
    change = change-(tenc*10)
    if tenc != 0:
        print(tenc, 'x 10c')
    fivec = change//5
    change = change-(fivec*5)
    if fivec != 0:
        print(fivec, "x 5c")
    if change !=0:
        print(change, "x 1c")
    